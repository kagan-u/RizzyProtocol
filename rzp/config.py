import random
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "rzp_config.json")

BASE_CONFIG = {
    "max_speed_bytes_per_sec": 1,
    "min_latency_seconds": 10,
    "packet_delay": 5,
    "handshake_steps": 42,
    "goodbye_steps": 84,
    "forget_clients": True,
    "forget_probability": 0.1,
    "duplication_probability": 0.15,
    "deletion_probability": 0.15,
    "inversion_probability": 0.1,
    "gaslight_probability": 0.2,
    "log_everything": True,
    "self_modify": True,
    "current_config": {}
}

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return BASE_CONFIG.copy()

def save_config(cfg):
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

config = load_config()

def randomly_modify():
    keys = list(config.keys())
    if random.random() < 0.3 and keys:
        key = random.choice(keys)
        val = config[key]
        if isinstance(val, bool):
            config[key] = not val
        elif isinstance(val, (int, float)):
            config[key] = val * random.uniform(0.5, 2.0)
        elif isinstance(val, str):
            config[key] = val[::-1]
    save_config(config)

def reload():
    global config
    config = load_config()
    randomly_modify()
