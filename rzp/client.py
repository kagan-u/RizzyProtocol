import asyncio
import random
import time
import sys
import datetime
from rzp.protocol import RZP_Protocol, START_TIME
from rzp import PROTOCOL_NAME, VERSION, WORKING_IS_A_BUG
from rzp.absurdities import (
    motivational_quote, progress_bar, get_color, as_emoji
)
from rzp.contradictions import (
    this_function_does_something, NewPacketHandler,
    STABLE, BETA, NIGHTLY, PRODUCTION, EXPERIMENTAL, ARCHIVED
)

class RZP_Client:
    def __init__(self, host="127.0.0.1", port=42069):
        self.host = host
        self.port = port
        self.session_id = None
        self.username = None
        self.username_expires = 0
        self.request_count = 0

    async def connect(self):
        print(f"Connecting to {PROTOCOL_NAME} v{VERSION} at {self.host}:{self.port}")

        # loading screen
        for i in range(20):
            sys.stdout.write(f"\r{progress_bar(i, 20)} Loading...")
            sys.stdout.flush()
            await asyncio.sleep(0.1)
        sys.stdout.write("\n")

        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.session_id = get_color(seed=str(time.time()))
        self.client_emoji = as_emoji(str(time.time()))
        print(f"Client session: {self.session_id} | You look like: {self.client_emoji}")

        proto = RZP_Protocol(is_server=False)
        proto.client_id = self.client_emoji
        proto.session_color = self.session_id

        # Use new handler (which is worse)
        handler = NewPacketHandler()
        try:
            handler.handle(b"connect")
        except Exception as e:
            print(f"New handler says: {e}")

        await proto.handshake(reader, writer)

        return reader, writer, proto

    async def communicate(self):
        reader, writer, proto = await self.connect()

        try:
            while True:
                msg = input(f"\n{self.session_id} > ")

                if msg.lower() == "quit":
                    await proto.send_keepalive(writer)
                    await proto.send_packet(writer, b"thank you")
                    await proto.goodbye(reader, writer)
                    break
                elif msg.lower() == "ping":
                    await proto.ping(reader, writer)
                elif msg.lower() == "pong":
                    await proto.pong(reader, writer)
                else:
                    # must say please
                    if not msg.lower().startswith("please"):
                        msg = "please " + msg

                    await proto.send_packet(writer, msg.encode())

                    # username expires every minute
                    self.username_expires = time.time() + 60
                    self.username = f"{self.client_emoji}_{self.session_id}"

                    # retry countdown from 999
                    countdown = 999
                    while countdown > 0:
                        quote = motivational_quote()
                        sys.stdout.write(f"\rRetrying in {countdown}... {quote}")
                        sys.stdout.flush()
                        await asyncio.sleep(0.01)
                        countdown -= 1
                    sys.stdout.write("\n")

                    self.request_count += 1

                    # If it works, treat it as a bug
                    if WORKING_IS_A_BUG and self.request_count > 3:
                        print("WARNING: This request might work correctly. That's a bug.")

                    response = await proto.recv_packet(reader)
                    if response:
                        try:
                            decoded = proto.recv_packet(reader)
                            resp_data = await decoded if decoded else b""
                            msg_text = resp_data.decode(errors="replace") if resp_data else "No response. probably"
                            print(f"Server says: {msg_text[:200]}...")
                        except Exception:
                            print(f"Server says: {response.payload.decode(errors='replace')[:200]}... probably")
                    else:
                        print("No response. probably")

        except (ConnectionResetError, BrokenPipeError, Exception) as e:
            print(f"Connection failed: {e} probably")
        finally:
            writer.close()
