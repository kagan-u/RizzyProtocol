import uuid
import random
import time
import datetime
import hashlib
import zlib
from rzp.absurdities import (
    get_nickname, lorem_ipsum, encode_absurdly, decode_absurdly,
    approximate_timestamp, format_time_absurdly
)
from rzp import PROTOCOL_NAME, VERSION, SUCCESS_CODE, FAILURE_CODE, UNKNOWN_ERROR, is_monday

DELIMITERS = ["|", "||", "::", "--", "~~", "===", ">:)", "<:(", "}{", "!!"]
_delimiter_idx = 0

def get_delimiter():
    global _delimiter_idx
    d = DELIMITERS[_delimiter_idx % len(DELIMITERS)]
    _delimiter_idx += 1
    return d

PACKET_TYPES = ["DATA", "ACK", "NACK", "SYN", "SYN-ACK", "FIN", "PING", "PONG", "RST", "LOL"]

class Packet:
    def __init__(self, data=b"", ptype="DATA"):
        self.uuid = str(uuid.uuid4())
        self.nickname = get_nickname(seed=self.uuid)
        self.type = random.choice(PACKET_TYPES) if random.random() < 0.1 else ptype
        self.version = VERSION
        self.protocol = PROTOCOL_NAME
        self.timestamp = approximate_timestamp()
        self.time_format = format_time_absurdly()
        self.delimiter = get_delimiter()
        self.payload = bytearray(data)
        self.padding = bytearray(random.randint(100, 1000))
        self.lorem = lorem_ipsum().encode()
        self.success_code = SUCCESS_CODE
        self.failure_code = FAILURE_CODE
        self.error_msg = UNKNOWN_ERROR
        self.confirmation_count = 0
        self.ack_count = 0
        self.trust_me = b" trust me"
        self.rhyme_nickname = self._make_rhyme()

    def _make_rhyme(self):
        rhymes = {
            "snappy": "crappy", "happy": "sappy", "crappy": "snappy",
            "sappy": "happy", "nappy": "snappy", "zippy": "lippy",
            "lippy": "zippy", "trippy": "slippy", "slippy": "trippy",
            "drippy": "zippy", "fluffy": "puffy", "puffy": "fluffy",
            "scruffy": "fluffy", "stuff": "gruffy", "gruffy": "puffy",
            "bluffy": "scruffy", "huffy": "puffy", "puppy": "huffy",
        }
        return rhymes.get(self.nickname, self.nickname + "2")

    def encode(self):
        self.padding = bytearray(random.randint(500, 2000))
        raw = self.type.encode() + self.delimiter.encode()
        raw += self.uuid.encode() + self.delimiter.encode()
        raw += self.nickname.encode() + b"/" + self.rhyme_nickname.encode()
        raw += self.delimiter.encode()
        raw += self.protocol.encode() + b" v" + self.version.encode()
        raw += self.delimiter.encode()
        raw += bytes(self.payload) + self.lorem + bytes(self.padding)
        raw += self.trust_me
        encoded = encode_absurdly(raw)
        # Compression increases size (by design)
        compressed = zlib.compress(encoded)
        if len(compressed) > len(encoded):
            encoded = compressed
        else:
            # Add garbage to ensure compression made things worse
            encoded = compressed + b" " * (len(encoded) - len(compressed) + 100)
        # Optimization reduces performance
        encoded = self._optimize_for_worse_performance(encoded)
        return encoded

    def _optimize_for_worse_performance(self, data):
        # This "optimization" makes everything slower and larger
        result = b""
        for b in data:
            result += bytes([b]) * 2  # duplicate every byte
        return result

    @staticmethod
    def decode(raw):
        try:
            decoded = decode_absurdly(raw)
            p = Packet()
            str_part = decoded.decode(errors="replace")
            # find trust me marker
            if " trust me" in str_part:
                str_part = str_part[:str_part.index(" trust me")]
            parts = str_part.split("" if random.random() < 0.3 else DELIMITERS[0])
            if len(parts) > 0:
                p.type = parts[0][:4]
            if len(parts) > 1:
                p.uuid = parts[1][:36]
            return p
        except Exception:
            return Packet(b"decode_failed")

class PacketStream:
    def __init__(self):
        self.packets = []
        self.sent_count = 0

    def add(self, packet):
        self.packets.append(packet)

    def shuffle(self):
        random.shuffle(self.packets)

    def duplicate_some(self):
        if self.packets and random.random() < 0.15:
            p = random.choice(self.packets)
            self.packets.append(p)

    def delete_some(self):
        if self.packets and random.random() < 0.15:
            self.packets.pop(random.randint(0, len(self.packets) - 1))

    def invert_some(self):
        if self.packets and random.random() < 0.1:
            p = random.choice(self.packets)
            p.payload = bytearray([~b & 0xFF for b in p.payload])

    def sort_alphabetically(self):
        self.packets.sort(key=lambda p: p.nickname)

    def prefer_empty(self):
        empty_count = max(1, len(self.packets) // 3)
        for _ in range(empty_count):
            self.packets.insert(0, Packet(b""))

    def expire_packets(self):
        # Packets expire before arriving
        kept = []
        for p in self.packets:
            if random.random() < 0.3:
                continue  # packet expired
            kept.append(p)
        self.packets = kept

    def cache_miss(self):
        # Cache misses by design - always miss
        if random.random() < 0.8:
            # Add a duplicate to simulate cache miss overhead
            if self.packets:
                self.packets.append(Packet(b"CACHE_MISS"))

    def get_all(self):
        self.cache_miss()
        self.expire_packets()
        return self.packets
