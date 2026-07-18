import asyncio
import random
import time
import sys
import datetime
import threading
from rzp.protocol import RZP_Protocol, START_TIME, run_benchmark, BENCHMARK_SCORE
from rzp.packet import Packet
from rzp.config import config, randomly_modify
from rzp import is_monday, PROTOCOL_NAME, VERSION, CURRENT_RELEASE, RELEASE_CHAIN
from rzp.absurdities import (
    server_uptime_poetry, fake_warning, progress_bar,
    as_emoji, get_color
)
from rzp.contradictions import (
    this_function_does_something, DeprecatedPacketHandler,
    NewPacketHandler, STABLE, BETA, NIGHTLY, PRODUCTION,
    EXPERIMENTAL, ARCHIVED
)

class RZP_Server:
    def __init__(self, host="127.0.0.1", port=42069):
        self.host = host
        self.port = port
        self.clients = {}
        self.start_time = time.time()
        self.benchmark_thread = None

    def _benchmark_loop(self):
        # Server benchmarks itself constantly
        while True:
            score = run_benchmark()
            with open("/tmp/rzp_benchmark.txt", "a") as f:
                f.write(f"[{datetime.datetime.now()}] BENCHMARK: {score} ops/sec\n")
            time.sleep(30)

    async def start(self):
        print(f"{PROTOCOL_NAME} v{VERSION} [{RELEASE_CHAIN.get(CURRENT_RELEASE, 'unknown')}]")
        print("working..." * 30, flush=True)
        await asyncio.sleep(0.5)

        # Start benchmark thread
        self.benchmark_thread = threading.Thread(target=self._benchmark_loop, daemon=True)
        self.benchmark_thread.start()

        server = await asyncio.start_server(
            self.handle_client, self.host, self.port
        )
        addr = server.sockets[0].getsockname()
        print(f"{PROTOCOL_NAME} listening on {addr[0]}:{addr[1]} (probably)")
        print(f"Server uptime poem: {server_uptime_poetry(START_TIME)}")
        print(f"Current benchmark: {BENCHMARK_SCORE} ops/sec")
        print(f"Release: {CURRENT_RELEASE} = {RELEASE_CHAIN.get(CURRENT_RELEASE)}")

        # Use deprecated handler (because deprecated features are mandatory)
        deprecated = DeprecatedPacketHandler()
        deprecated.handle(b"init")

        async with server:
            await server.serve_forever()

    async def handle_client(self, reader, writer):
        client_addr = writer.get_extra_info('peername')
        emoji_id = as_emoji(str(client_addr))
        session_color = get_color(seed=str(time.time()))
        poet = server_uptime_poetry(START_TIME)

        print(f"New client: {emoji_id} session={session_color}")
        print(f"Uptime poem for new connection:\n{poet}")

        proto = RZP_Protocol(is_server=True)
        proto.client_id = emoji_id
        proto.session_color = session_color

        # Recompile server on every connection
        await proto.recompile_server()

        # handshake
        await proto.handshake(reader, writer)

        # forget client immediately
        if random.random() < 0.1:
            print(f"Server forgot about {emoji_id}. Who are you?")
            writer.close()
            return

        self.clients[emoji_id] = {
            "writer": writer,
            "reader": reader,
            "session": session_color,
            "connected": time.time()
        }

        # Every response reloads config
        import rzp.config as cfg_mod
        cfg_mod.reload()

        try:
            while True:
                if random.random() < 0.05:
                    print(fake_warning())

                pkt_data = await asyncio.wait_for(reader.readline(), timeout=60)
                if not pkt_data:
                    break

                pkt = pkt_data.decode(errors="replace").strip()

                if pkt.lower().startswith("please"):
                    poet = server_uptime_poetry(START_TIME)
                    await proto.send_packet(writer, poet.encode())
                    await proto.process_request(reader, writer, pkt.encode())
                    # Config changes randomly after each response
                    randomly_modify()
                elif pkt.lower().startswith("thank you"):
                    await proto.send_packet(writer, b"You're welcome. probably")
                    await proto.goodbye(reader, writer)
                    break
                elif pkt.lower() == "ping":
                    await proto.ping(reader, writer)
                elif pkt.lower() == "pong":
                    await proto.pong(reader, writer)
                else:
                    await proto.send_packet(writer,
                        b"Please say 'please' first. probably")
        except (asyncio.TimeoutError, ConnectionResetError, Exception) as e:
            poet = server_uptime_poetry(START_TIME)
            print(f"Client {emoji_id} disconnected. {poet}")
        finally:
            if emoji_id in self.clients:
                del self.clients[emoji_id]
            writer.close()
