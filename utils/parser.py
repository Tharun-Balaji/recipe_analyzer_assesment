from ast import Return
import json


class ResponseParser:
    """Handles parsing of API responses and recipe data."""
    
    def parse_api_response(self, response_text):
        # TODO: Clean the response text using clean_response_text
        
        # TODO: Parse the cleaned text as JSON using json.loads
        
        # TODO: Check if parsed result has "analysis" key with list value
        #       Return the analysis list if found
        
        # TODO: Handle JSONDecodeError by returning empty list
        
        pass
    
    def clean_response_text(self, text):
        # TODO: Strip whitespace from text
        
        # TODO: Remove "```json" or "```" from the beginning if present
        
        # TODO: Remove "```" from the end if present
        
        # TODO: Return cleaned and stripped text
        
        pass