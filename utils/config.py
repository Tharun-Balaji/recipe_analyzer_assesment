import os

def load_system_prompt() -> str:
    """Load the system prompt from prompt.txt file."""
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompt.txt")
    try:
        with open(prompt_path, encoding="utf-8") as prompt_file:
            return prompt_file.read().strip()
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "prompt.txt file not found. Please ensure it exists in the solution directory"
        ) from error
    except OSError as error:
        raise OSError(f"Error loading prompt.txt: {error}") from error


def get_system_prompt() -> str:
    """Get the system prompt with recipes placeholder."""
    return load_system_prompt()


# Export the system prompt
SYSTEM_PROMPT = get_system_prompt()
