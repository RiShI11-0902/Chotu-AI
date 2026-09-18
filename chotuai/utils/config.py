import json
from pathlib import Path


CONFIG_DIR = Path.home() / ".chotuai"
CONFIG_FILE = CONFIG_DIR / "config.json"


def save_config(provider, model):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config = {
        "provider": provider,
        "model": model
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

    print(f"Configuration saved to: {CONFIG_FILE}")


def load_config():
    if not CONFIG_FILE.exists():
        return None

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)