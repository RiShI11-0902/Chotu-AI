import requests

from chotuai.utils.config import save_config


OLLAMA_URL = "http://localhost:11434"


def setup_ollama():

    print("\nChecking Ollama...")

    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=5
        )

        response.raise_for_status()

    except requests.RequestException:
        print("\nOllama is not running or could not be reached.")
        return

    data = response.json()

    models = data.get("models", [])

    if not models:
        print("No Ollama models found.")
        print("Please install an Ollama model first.")
        return

    print("\nAvailable Ollama models:\n")

    for index, model in enumerate(models, start=1):
        print(f"{index}. {model['name']}")

    while True:
        try:
            choice = int(input("\nChoose a model: "))

            if 1 <= choice <= len(models):
                selected_model = models[choice - 1]["name"]
                break

            print("Please choose a valid number.")

        except ValueError:
            print("Please enter a number.")

    save_config("ollama", selected_model)

    print("\n✓ ChotuAI setup completed.")
    print(f"Provider: Ollama")
    print(f"Model: {selected_model}")