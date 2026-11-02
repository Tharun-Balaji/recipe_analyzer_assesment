import os
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT
from utils.parser import ResponseParser

load_dotenv()

class RecipeBatchAnalyzer:
    """Analyzes multiple recipes in a single batch using Gemini API."""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=self.api_key)
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.parser = ResponseParser()
    
    def format_recipes_for_analysis(self, recipes):
        """Format recipes for batch analysis."""
        formatted_recipes = []
        for number, recipe in enumerate(recipes, start=1):
            name = recipe.get("name") or "Unknown"
            ingredients = recipe.get("ingredients") or []
            instructions = recipe.get("instructions") or "No instructions provided"
            formatted_recipes.append(
                "\n".join(
                    [
                        f"Recipe {number}: {name}",
                        f"Ingredients: {', '.join(ingredients)}",
                        f"Instructions: {instructions}",
                    ]
                )
            )
        return "\n\n".join(formatted_recipes)
    
    def analyze_batch(self, recipes):
        """Analyze a batch of recipes."""
        if not recipes:
            return {"batch_id": "empty_batch", "total_recipes": 0, "analysis": []}

        limited_recipes = recipes[:5]
        formatted_recipes = self.format_recipes_for_analysis(limited_recipes)
        full_prompt = SYSTEM_PROMPT.format(recipes=formatted_recipes)
        response = self.client.models.generate_content(
            model=self.model,
            contents=full_prompt,
        )
        analysis = self.parser.parse_api_response(response)

        return {
            "batch_id": f"batch_{hash(str(recipes)) % 10000}",
            "total_recipes": len(limited_recipes),
            "analysis": analysis[: len(limited_recipes)],
        }
    
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