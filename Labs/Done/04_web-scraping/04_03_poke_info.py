# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests

BASE_URL = "https://pokeapi.co/api/v2/"

# Choose your 6 favorite Pokémon
favorite_pokemon = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar", "snorlax"]

team_data = []

print("Fetching Pokémon team data...\n")
for name in favorite_pokemon:
    response = requests.get(f"{BASE_URL}pokemon/{name}")
    if response.status_code == 200:
        data = response.json()

        # Extract required information
        pokemon_info = {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "types": [t["type"]["name"].capitalize() for t in data["types"]],
            "sprite": data["sprites"]["front_default"]
        }
        team_data.append(pokemon_info)

        print(f"Fetched: {pokemon_info['name']} (#{pokemon_info['id']}) - Types: {', '.join(pokemon_info['types'])}")
    else:
        print(f"Failed to fetch data for {name}")

# Build a small HTML page to display the team with sprites
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Pokémon Team</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding: 20px; }
        .team-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
        .pokemon-card { background: white; border-radius: 10px; padding: 15px; width: 180px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .pokemon-card img { width: 120px; height: 120px; }
        h2 { color: #333; margin: 10px 0 5px 0; }
        p { color: #666; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>My Ultimate Pokémon Team</h1>
    <div class="team-container">
"""

for p in team_data:
    html_content += f"""
        <div class="pokemon-card">
            <img src="{p['sprite']}" alt="{p['name']}">
            <h2>{p['name']}</h2>
            <p><strong>No.</strong> {p['id']}</p>
            <p><strong>Types:</strong> {', '.join(p['types'])}</p>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

# Write the HTML content to a local file
with open("pokemon_team.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("\nSuccess! Team information has been saved and rendered to 'pokemon_team.html'.")
