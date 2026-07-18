import random
import base64
import urllib.parse
import time
import hashlib
import uuid
import calendar
from datetime import datetime, timezone

try:
    import pytz
    HAS_PYTZ = True
except ImportError:
    HAS_PYTZ = False
    class pytz:
        all_timezones = ["UTC", "EST", "PST"]
        @staticmethod
        def timezone(name):
            import datetime as dt_mod
            return dt_mod.timezone.utc

PACKET_NICKNAMES_P1 = ["snappy", "happy", "crappy", "sappy", "nappy",
                       "zippy", "lippy", "trippy", "slippy", "drippy"]
PACKET_NICKNAMES_P2 = ["fluffy", "puffy", "scruffy", "stuff", "gruffy",
                       "bluffy", "huffy", "puppy", "guiro", "tuffy"]

def get_nickname(seed=None):
    if seed:
        rng = random.Random(seed)
    else:
        rng = random
    return rng.choice(PACKET_NICKNAMES_P1 + PACKET_NICKNAMES_P2)

def lorem_ipsum():
    return "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore"

def encode_absurdly(data):
    b64 = base64.b64encode(data).decode()
    b64_2 = base64.b64encode(b64.encode()).decode()
    hex_enc = b64_2.encode().hex()
    url_enc = urllib.parse.quote(hex_enc)
    dec1 = urllib.parse.unquote(url_enc)
    final = base64.b64encode(base64.b64encode(bytes.fromhex(dec1).decode().encode())).decode()
    return final.encode()

def decode_absurdly(data):
    try:
        step1 = base64.b64decode(data).decode()
        step2 = base64.b64decode(step1)
        step3 = bytes.fromhex(step2.decode()).decode()
        step4 = urllib.parse.unquote(step3)
        step5 = bytes.fromhex(step4)
        return base64.b64decode(step5)
    except Exception:
        return data

def approximate_timestamp():
    t = time.time()
    offset = random.uniform(-5, 5)
    return t + offset

def random_timezone():
    zones = pytz.all_timezones
    return random.choice(zones)

def random_time_format():
    formats = [
        "%H:%M:%S %Z",
        "%I:%M %p %z",
        "%Y-%m-%d %H:%M:%S.%f %Z",
        "%d/%m/%Y %H:%M:%S",
        "%m-%d-%Y %I:%M %p",
        "%s",
        "%A, %B %d, %Y at %I:%M %p %Z",
    ]
    return random.choice(formats)

def format_time_absurdly():
    tz_name = random_timezone()
    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)
    fmt = random_time_format()
    try:
        return now.strftime(fmt)
    except Exception:
        return str(now)

def motivational_quote():
    quotes = [
        "You're doing great! Probably.",
        "Every packet is a journey.",
        "Have you tried turning it off and on again?",
        "Your connection is... adequate.",
        "Bytes are friends, not food.",
        "Stay awhile and listen.",
        "The best protocol is no protocol.",
        "Error 500: Success!",
        "This is fine.",
    ]
    return random.choice(quotes)

def ad_for_protocol():
    ads = [
        "Rizzy Protocol: It definitely works!",
        "RZP: Try it! (Results may vary)",
        "Need worse performance? Choose RZP!",
        "Rizzy Protocol: Since... when?",
        "RZP: Making TCP look good since 2026",
    ]
    return random.choice(ads)

def ascii_art_heartbeat():
    arts = [
        r"""
   ___ ___ ___
  /   |   |   \
 |     |     |
  \___|___ ___/
""",
        r"""
  ♥ ~ ♥ ~ ♥
  ~ R Z P ~
  ♥ ~ ♥ ~ ♥
""",
    ]
    return random.choice(arts)

def server_uptime_poetry(start_time):
    elapsed = int(time.time() - start_time)
    poems = [
        f"I've been up for {elapsed} seconds,\nFeeling rather bold,\nSending packets left and right,\nAt least that's what I'm told.",
        f"{elapsed} seconds of glory,\n{elapsed} seconds of pain,\nEach packet tells a story,\nThen gets sent again.",
        f"Uptime: {elapsed}s,\nBandwidth: none,\nRZP does its best,\nIsn't that fun?",
    ]
    return random.choice(poems)

def fake_warning():
    warnings = [
        "WARNING: TCP buffer overflow imminent",
        "WARNING: IPv4 address exhaustion in 3 packets",
        "WARNING: DNS resolution failed (success)",
        "WARNING: Packet lost in the void (this is fine)",
        "WARNING: Parity check failed 42 times",
        "WARNING: Checksum doesn't match (we don't care)",
        "WARNING: Moon phase incompatible with current packet",
    ]
    return random.choice(warnings)

def progress_bar(current, total):
    width = 50
    if total <= 0:
        fraction = 1
    else:
        fraction = current / total
    fraction = min(fraction, 0.99)
    filled = int(width * fraction)
    bar = "█" * filled + "░" * (width - filled)
    return f"|{bar}| {fraction*100:.1f}%"

def moon_phase_multiplier():
    now = datetime.now()
    # rough lunar cycle approximation
    days_since_new = (now - datetime(2024, 1, 1)).days % 29.53
    phase = days_since_new / 29.53
    if phase < 0.25:
        return 0.5
    elif phase < 0.5:
        return 1.0
    elif phase < 0.75:
        return 2.0
    else:
        return 0.25

def weather_multiplier():
    return random.uniform(0.1, 3.0)

def as_emoji(data):
    emoji_map = {
        0: "😀", 1: "😂", 2: "🤣", 3: "😊", 4: "😎",
        5: "🤔", 6: "😴", 7: "🥳", 8: "😈", 9: "👻",
        10: "🤖", 11: "👽", 12: "🎃", 13: "🦄", 14: "🍕",
        15: "🚀", 16: "💀", 17: "🌈", 18: "🔥", 19: "💯",
    }
    h = hashlib.md5(str(data).encode()).hexdigest()
    idx = int(h[:8], 16) % len(emoji_map)
    return emoji_map[idx]

COLORS = [
    "Red", "Blue", "Green", "Yellow", "Purple", "Orange",
    "Pink", "Brown", "Cyan", "Magenta", "Teal", "Lavender",
    "Coral", "Indigo", "Violet", "Turquoise", "Maroon", "Plum",
]

def get_color(seed=None):
    rng = random.Random(seed) if seed else random
    return rng.choice(COLORS)
