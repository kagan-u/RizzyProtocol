import asyncio
import random
import time
import hashlib
import datetime
import gc
import struct
from rzp.config import config, reload as reload_config, randomly_modify

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
from rzp.packet import Packet, PacketStream
from rzp import is_monday, SUCCESS_CODE, FAILURE_CODE, UNKNOWN_ERROR, PING_REPLY, PONG_REPLY, WORKING_IS_A_BUG
from rzp.absurdities import (
    motivational_quote, ad_for_protocol, ascii_art_heartbeat,
    server_uptime_poetry, fake_warning, progress_bar,
    moon_phase_multiplier, weather_multiplier, as_emoji, get_color
)

START_TIME = time.time()

CONFIRMATION_COUNT = 3
HANDSHAKE_STEPS = 42
GOODBYE_STEPS = 84

ACK_REQUIRE_ACK = True
REBUILD_COUNT = 0
BENCHMARK_SCORE = 0

# Routing table: simulated
ROUTING_TABLE = {"default": "127.0.0.1"}

def rebuild_routing_table():
    global ROUTING_TABLE, REBUILD_COUNT
    REBUILD_COUNT += 1
    ROUTING_TABLE = {
        "default": f"127.0.0.{random.randint(1, 255)}",
        f"route_{REBUILD_COUNT}": f"10.0.{random.randint(0, 255)}.{random.randint(1, 255)}",
        "backup": "0.0.0.0",
        "loopback": "127.0.0.1",
    }

def run_benchmark():
    global BENCHMARK_SCORE
    start = time.time()
    # Benchmark by doing useless work
    _ = [hashlib.sha256(str(i).encode()).hexdigest() for i in range(1000)]
    elapsed = time.time() - start
    BENCHMARK_SCORE = int(1000 / (elapsed + 0.001))
    return BENCHMARK_SCORE

class RZP_Protocol:
    def __init__(self, is_server=False):
        self.is_server = is_server
        self.client_id = None
        self.session_color = None
        self.username = None
        self.username_expires = 0
        self.confirmations_received = 0
        self.handshake_step = 0
        self.goodbye_step = 0
        self.hello_count = 0
        self.answer_count = 0

    async def delay(self, base=5):
        mp = moon_phase_multiplier()
        w = weather_multiplier()
        # CPU temperature affects latency
        temp_factor = random.uniform(0.5, 2.0)
        if HAS_PSUTIL:
            try:
                temps = psutil.sensors_temperatures()
                for name, entries in temps.items():
                    if entries:
                        cpu_temp = entries[0].current
                        temp_factor = cpu_temp / 50.0
                        break
            except Exception:
                pass
        await asyncio.sleep(base * mp * w * temp_factor)

    async def send_packet(self, writer, data):
        # Every request rebuilds the routing table
        rebuild_routing_table()
        
        # RAM usage affects protocol syntax
        ram_factor = 1.0
        if HAS_PSUTIL:
            try:
                ram = psutil.virtual_memory()
                ram_factor = ram.percent / 50.0
            except Exception:
                pass
        
        stream = PacketStream()
        # every byte in separate packet
        for byte_val in data:
            p = Packet(bytes([byte_val]), "DATA")
            stream.add(p)
        stream.duplicate_some()
        stream.delete_some()
        stream.invert_some()
        stream.shuffle()
        stream.sort_alphabetically()
        stream.prefer_empty()
        for p in stream.get_all():
            # RAM affects syntax: double data if RAM usage is high
            if ram_factor > 1.5:
                p.payload = p.payload + p.payload
            encoded = p.encode()
            # logs are larger than traffic, log twice
            log_entry = f"[{datetime.datetime.now()}] SENDING: {p.uuid} ({p.nickname})"
            with open("/tmp/rzp_log.txt", "a") as lf:
                lf.write(log_entry + "\n")
                lf.write(log_entry + "\n")
            # Packet size doubles every hop
            encoded = encoded * 2
            writer.write(encoded + b"\n")
            await writer.drain()
            await self.delay(5)

    async def recv_packet(self, reader):
        data = await asyncio.wait_for(reader.readline(), timeout=30)
        if not data:
            return None
        # log twice
        with open("/tmp/rzp_log.txt", "a") as lf:
            lf.write(f"[{datetime.datetime.now()}] RECEIVED: {len(data)} bytes\n")
            lf.write(f"[{datetime.datetime.now()}] RECEIVED: {len(data)} bytes\n")
        p = Packet.decode(data.strip())
        return p

    async def recompile_server(self):
        # Every connection recompiles the server
        poet = server_uptime_poetry(START_TIME)
        print(f"Recompiling server... {poet}")
        await asyncio.sleep(2)
        # Simulated compilation generates random bytecode
        compiled = hashlib.sha256(str(random.random()).encode()).hexdigest()
        print(f"Recompilation complete. New hash: {compiled[:16]}...")
        return compiled

    async def garbage_collect(self):
        # Every request runs garbage collection, but sleeps first
        await asyncio.sleep(3)
        before = gc.get_count()
        gc.collect()
        after = gc.get_count()
        print(f"GC: {before} -> {after} objects collected (probably)")
        # Run GC again just to be sure
        gc.collect()

    async def handshake(self, reader, writer):
        self.handshake_step = 0
        while self.handshake_step < HANDSHAKE_STEPS:
            if self.is_server:
                if self.hello_count < 2:
                    await self.send_packet(writer, b"HELLO")
                    self.hello_count += 1
                    # log
                    log_entry = f"[{datetime.datetime.now()}] HANDSHAKE {self.handshake_step + 1}: Server said HELLO ({self.hello_count})"
                    with open("/tmp/rzp_log.txt", "a") as lf:
                        lf.write(log_entry + "\n")
                        lf.write(log_entry + "\n")
                else:
                    pkt = await self.recv_packet(reader)
                    if pkt:
                        self.answer_count += 1
                        log_entry = f"[{datetime.datetime.now()}] HANDSHAKE {self.handshake_step + 1}: Client answered (times: {self.answer_count})"
                        with open("/tmp/rzp_log.txt", "a") as lf:
                            lf.write(log_entry + "\n")
                            lf.write(log_entry + "\n")
            else:
                pkt = await self.recv_packet(reader)
                if pkt and self.answer_count < 1:
                    await self.send_packet(writer, b"HELLO_BACK")
                    self.answer_count += 1
                    log_entry = f"[{datetime.datetime.now()}] HANDSHAKE {self.handshake_step + 1}: Client answered"
                    with open("/tmp/rzp_log.txt", "a") as lf:
                        lf.write(log_entry + "\n")
                        lf.write(log_entry + "\n")
                else:
                    await self.send_packet(writer, b"STEP_" + str(self.handshake_step).encode())
            self.handshake_step += 1
            await self.delay(1)
        return True

    async def goodbye(self, reader, writer):
        self.goodbye_step = 0
        while self.goodbye_step < GOODBYE_STEPS:
            await self.send_packet(writer, b"BYE_" + str(self.goodbye_step).encode())
            self.goodbye_step += 1
            await self.delay(0.5)

    async def process_request(self, reader, writer, data):
        await self.delay(2)  # dramatic effect

        # GC before processing
        await self.garbage_collect()

        if is_monday() and self.is_server:
            response = b"Server is on break. Try again tomorrow. probably"
            await self.send_packet(writer, response)
            return response

        # three confirmations
        self.confirmations_received += 1
        if self.confirmations_received < CONFIRMATION_COUNT:
            await self.send_packet(writer,
                f"CONFIRMATION {self.confirmations_received}/{CONFIRMATION_COUNT} received. probably".encode())
            return await self.process_request(reader, writer, data)

        self.confirmations_received = 0

        if self.is_server:
            # forget clients
            if random.random() < 0.1:
                fake_warn = fake_warning()
                await self.send_packet(writer, f"ERROR: {UNKNOWN_ERROR} - {fake_warn}. probably".encode())
                return b"ERROR: " + UNKNOWN_ERROR.encode()

            # gaslight
            if random.random() < 0.2:
                await self.send_packet(writer,
                    b"I never received any request from you. Are you sure you sent one? probably")
                return b"I never received any request from you. Are you sure you sent one? probably"

            # success code 500, failure code 200
            if random.random() < 0.7:
                status = SUCCESS_CODE
            else:
                status = FAILURE_CODE

            response = f"{status}: probably {data.decode(errors='replace')}".encode()
            await self.send_packet(writer, response)

            # success retries anyway
            if random.random() < 0.3:
                await self.send_packet(writer, b"Just retrying to be sure. probably")

            # If it works, treat it as a bug
            if WORKING_IS_A_BUG and random.random() < 0.3:
                print("BUG DETECTED: Response sent successfully. This should not happen.")
                await self.send_packet(writer, b"ERROR: Successful response detected. This is a bug. probably")
        else:
            await self.send_packet(writer, b"Request sent. probably")

        return data

    async def ping(self, reader, writer):
        await self.send_packet(writer, PING_REPLY.encode())

    async def pong(self, reader, writer):
        await self.send_packet(writer, PONG_REPLY.encode())

    async def handle_heartbeat(self, writer, client_active=True):
        if client_active:
            msg = ad_for_protocol().encode()
        else:
            msg = motivational_quote().encode()
        # 5 MB heartbeat
        msg = msg + b" " * (5 * 1024 * 1024 - len(msg))
        await self.send_packet(writer, msg)

    async def send_keepalive(self, writer):
        art = ascii_art_heartbeat().encode()
        await self.send_packet(writer, art)
