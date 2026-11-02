import json


class ResponseParser:
    """Handles parsing of API responses and recipe data."""
    
    def parse_api_response(self, response_text):
        try:
            text = response_text.text if hasattr(response_text, "text") else response_text
            if not isinstance(text, str):
                return []
            parsed_response = json.loads(self.clean_response_text(text))
        except (json.JSONDecodeError, TypeError):
            return []

        analysis = parsed_response.get("analysis") if isinstance(parsed_response, dict) else None
        return analysis if isinstance(analysis, list) else []
    
    def clean_response_text(self, text):
        cleaned_text = text.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[len("```json"):]
        elif cleaned_text.startswith("```"):
            cleaned_text = cleaned_text[len("```"):]
        if cleaned_text.rstrip().endswith("```"):
            cleaned_text = cleaned_text.rstrip()[:-3]
        return cleaned_text.strip()