
import requests
OLLAMA_URL = 'http://localhost:11434/api/generate'
from chotuai.utils.config import load_config

def call_ollama(prompt):

    config = load_config()

    if config is None:
        print("ChotuAI is not configured.")
        print("Run: chotuai setup")
        return None

    model = config["model"]

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]