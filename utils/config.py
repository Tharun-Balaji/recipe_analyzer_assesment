import os

def load_system_prompt() -> str:
    """Load the system prompt from prompt.txt file."""
    # TODO: Get the path to prompt.txt file in the parent directory
    
    # TODO: Open and read the prompt file with proper encoding
    
    # TODO: Return the content stripped of whitespace
    
    # TODO: Handle FileNotFoundError with appropriate message: "prompt.txt file not found. Please ensure it exists in the solution directory"
    
    # TODO: Handle other exceptions with appropriate message: "Error loading prompt.txt: {error_message}"
    
    pass


def get_system_prompt() -> str:
    """Get the system prompt with recipes placeholder."""
    # TODO: Call load_system_prompt() and return the result
    pass


# Export the system prompt
SYSTEM_PROMPT = get_system_prompt()
