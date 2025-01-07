from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TheMealDB API URL
THEMEALDB_API_URL = "https://www.themealdb.com/api/json/v1/1/search.php?s="

# Spoonacular API URL and API key
SPOONACULAR_API_KEY = "ef4c2a8e040543cc8dfc5924ad0a24f4"  # Replace with your key
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/complexSearch"

# Store saved favorites
favorites = []  # Added favorites functionality


@app.route("/")
def home():
    return "Welcome to the Recipe Finder Chatbot!"


@app.route("/chat", methods=["POST"])
def chat():
    # Get user input
    data = request.get_json()
    query = data.get("message")
    filters = data.get("filters", {})  # Added filters support

    if not query:
        return jsonify({"error": "Please provide a valid input."})

    try:
        # Trigger loading animation by sending status
        yield jsonify({"status": "loading"})  # Added loading status

        # Fetch recipe details from TheMealDB API
        themeal_response = requests.get(THEMEALDB_API_URL + query)
        themeal_result = themeal_response.json()

        # Check if recipe is found in TheMealDB
        if themeal_result['meals']:
            meal = themeal_result['meals'][0]
            title = meal['strMeal']
            category = meal['strCategory']
            area = meal['strArea']
            instructions = meal['strInstructions']
            image = meal['strMealThumb']
            source = meal['strSource'] if meal['strSource'] else "No source available"

            # Get ingredients and measurements
            ingredients = []
            for i in range(1, 21):
                ingredient = meal[f'strIngredient{i}']
                measure = meal[f'strMeasure{i}']
                if ingredient and ingredient.strip():
                    ingredients.append(f"{measure} {ingredient}")

            # Apply filters
            if filters:
                # Check cuisine
                if "cuisine" in filters and filters['cuisine'].lower() != area.lower():
                    return jsonify({"error": "No recipes match the specified cuisine."})
                # Check difficulty or prep time if provided
                # Placeholder logic (as difficulty/prep time is not supported by TheMealDB)

            return jsonify({
                "title": title,
                "category": category,
                "area": area,
                "ingredients": ingredients,
                "steps": instructions.split(". "),
                "link": source,
                "image": image
            })

        else:
            # Fetch recipe from Spoonacular if TheMealDB fails
            params = {
                'query': query,
                'apiKey': SPOONACULAR_API_KEY,
                'number': 4
            }

            # Apply filters for Spoonacular
            if "cuisine" in filters:
                params['cuisine'] = filters['cuisine']
            if "time" in filters:
                params['maxReadyTime'] = filters['time']
            if "difficulty" in filters:
                params['difficulty'] = filters['difficulty']  # Placeholder

            spoonacular_response = requests.get(SPOONACULAR_API_URL, params=params)
            spoonacular_result = spoonacular_response.json()

            # Check if recipe is found
            if spoonacular_result.get('results'):
                recipes = []
                for recipe in spoonacular_result['results']:
                    recipes.append({
                        "title": recipe['title'],
                        "image": recipe['image'],
                        "link": f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}"
                    })

                return jsonify({"recipes": recipes})

            else:
                return jsonify({"error": "Recipe not found. Try another dish!"})

    except Exception as e:
        return jsonify({"error": str(e)})


# Save Favorites Feature
@app.route("/save_favorite", methods=["POST"])
def save_favorite():
    data = request.get_json()
    recipe = data.get("recipe")

    if not recipe:
        return jsonify({"error": "No recipe provided to save."})

    favorites.append(recipe)  # Save to favorites list
    return jsonify({"message": "Recipe saved to favorites!"})


@app.route("/get_favorites", methods=["GET"])
def get_favorites():
    return jsonify({"favorites": favorites})


if __name__ == "__main__":
    app.run(debug=True)
