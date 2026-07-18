import random
import datetime

PROTOCOL_NAMES = [
    "Rizzy Protocol", "Absolute Protocol", "Definitely Protocol",
    "Trust Me Protocol", "Probably Protocol", "Maybe Protocol",
    "RZP", "NotTCP", "KindaUDP", "SortaHTTP"
]

def get_protocol_name():
    return random.choice(PROTOCOL_NAMES)

def get_version():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

PROTOCOL_NAME = get_protocol_name()
VERSION = get_version()
SUCCESS_CODE = 500
FAILURE_CODE = 200
UNKNOWN_ERROR = "Unknown Error"
PING_REPLY = "maybe"
PONG_REPLY = "nah"

def is_monday():
    return datetime.datetime.now().weekday() == 0

# Release stability inversion (as documented in contradictions.py)
RELEASE_CHAIN = {
    "stable": "Crashes proudly",
    "beta": "More stable than stable",
    "nightly": "Production-ready",
    "production": "Experimental - may work",
    "experimental": "Archived - do not use",
    "archived": "RECOMMENDED",
}
CURRENT_RELEASE = "stable"

# FIXME: Deprecated features are mandatory
# TODO: Remove this once deprecated features are fully implemented
DEPRECATED_FEATURES = {
    "old_handshake": True,
    "legacy_encoding": True,
    "v0_packet_format": True,
}

# If it works, treat it as a bug
WORKING_IS_A_BUG = True
