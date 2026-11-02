import os
from dotenv import load_dotenv
from google import genai
# TODO: Import SYSTEM_PROMPT from utils.config
# TODO: Import ResponseParser from utils.parser

# TODO: Load environment variables

class RecipeBatchAnalyzer:
    """Analyzes multiple recipes in a single batch using Gemini API."""
    
    def __init__(self, api_key=None):
        # TODO: Initialize API key from parameter or env var GEMINI_API_KEY
        self.api_key = None

        # TODO: Raise ValueError if no key found with the message "GEMINI_API_KEY not found"
        
        # TODO: Initialize Gemini client
        self.client = None

        # TODO: Set model from env var or default to "gemini-2.5-flash"
        self.model = None

        # TODO: Initialize ResponseParser
        self.parser = None
    
    def format_recipes_for_analysis(self, recipes):
        """Format recipes for batch analysis."""
        # TODO: Create a list to store formatted recipes
        # TODO: Loop through recipes with enumerate starting from 1 and format each as:
        # Recipe {number}: {name}
        # Ingredients: {ingredients}
        # Instructions: {instructions}
        # Use "Unknown" for missing name, [] for missing ingredients,
        # and "No instructions provided" for missing instructions.
        # Join ingredients with commas and formatted recipes with "\n\n".
        pass
    
    def analyze_batch(self, recipes):
        """Analyze a batch of recipes."""
    
        # TODO: If recipes is empty, return:
        # {"batch_id": "empty_batch", "total_recipes": 0, "analysis": []}

        # TODO: Limit the batch to the first 5 recipes for API efficiency.

        # TODO: Format the recipes using format_recipes_for_analysis().

        # TODO: Create the prompt using SYSTEM_PROMPT.format(recipes=formatted_recipes).

        # TODO: Call Gemini API with model and the generated prompt.

        # TODO: Parse response using parser.parse_api_response

        # TODO: Return a dictionary with:
        # "batch_id" as "batch_{hash(str(recipes)) % 10000}",
        # "total_recipes" as the number of recipes,
        # and "analysis" containing analysis results limited to the number of recipes.

        pass
    
def main():
    """Main function to demonstrate the recipe analyzer."""
    sample_recipes = [
        {
            "name": "Spaghetti Carbonara",
            "ingredients": ["spaghetti", "eggs", "bacon", "parmesan", "black pepper"],
            "instructions": "Cook pasta, fry bacon, mix with eggs and cheese"
        },
        {
            "name": "Caesar Salad",
            "ingredients": ["lettuce", "croutons", "parmesan", "caesar dressing"],
            "instructions": "Chop lettuce, add toppings, toss with dressing"
        },
        {
            "name": "Chocolate Chip Cookies",
            "ingredients": ["flour", "butter", "sugar", "chocolate chips", "eggs"],
            "instructions": "Mix ingredients, form cookies, bake at 350F"
        }
    ]
    
    print("Recipe Batch Analyzer")
    print("=" * 50)
    
    analyzer = RecipeBatchAnalyzer()
    
    try:
        result = analyzer.analyze_batch(sample_recipes)
        print(f"Analyzed {result.get('total_recipes', 0)} recipes")
        print("\nResults:")
        for recipe_analysis in result.get('analysis', []):
            name = recipe_analysis.get('recipe_name', 'Unknown')
            difficulty = recipe_analysis.get('difficulty', 'unknown')
            time = recipe_analysis.get('cooking_time', 'unknown')
            calories = recipe_analysis.get('calories_per_serving', 'unknown')
            print(f"- {name}: {difficulty} difficulty, {time}, ~{calories} calories")
    except Exception as e:
        print(f"Error analyzing recipes: {str(e)}")


if __name__ == "__main__":
    main()