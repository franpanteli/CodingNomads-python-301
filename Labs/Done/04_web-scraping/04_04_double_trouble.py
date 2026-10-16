# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

GHIBLI_URL = "https://ghibliapi-iansedano.vercel.app"
POKE_URL = "https://pokeapi.co/api/v2/"

print("=" * 50)
print("SPIRIT WORLD CROSSOVER: GHIBLI SPIRITS VS. GHOST POKÉMON")
print("=" * 50)

# --- PART 1: Fetch Ghibli Spirits / Mysterious Entities ---
print("\n[1] Fetching mystical entities from Studio Ghibli films...")
species_response = requests.get(f"{GHIBLI_URL}/species")
species_list = species_response.json()

ghibli_spirits = []
for species in species_list:
    # Looking for categories like 'Spirit', 'Deity', or magical beings
    name = species.get("name", "").lower()
    if "spirit" in name or "deity" in name or "ghost" in name:
        people_urls = species.get("people", [])
        for url in people_urls:
            char_id = url.split("/")[-1]
            char_res = requests.get(f"{GHIBLI_URL}/people/{char_id}")
            if char_res.status_code == 200:
                char_data = char_res.json()
                ghibli_spirits.append({
                    "name": char_data.get("name"),
                    "age": char_data.get("age"),
                    "gender": char_data.get("gender"),
                    "category": species.get("name")
                })

# Fallback if specific spirit species query yields broad data, let's grab a few iconic ones directly if needed
if not ghibli_spirits:
    # Grab a sample person endpoint or filter characters
    people_res = requests.get(f"{GHIBLI_URL}/people")
    if people_res.status_code == 200:
        all_people = people_res.json()
        # Filter for known spiritual or non-human entities
        ghibli_spirits = [
            {"name": p["name"], "age": p["age"], "gender": p["gender"], "category": "Mystical Entity"}
            for p in all_people if p["name"] in ["No-Face", "Haku", "Calcifer", "The Radish Spirit"]
        ]

print(f"-> Found {len(ghibli_spirits)} Ghibli entities/spirits:")
for spirit in ghibli_spirits[:3]: # Display first few
    print(- f"   • {spirit['name']} (Classification: {spirit['category']})")


# --- PART 2: Fetch an Opposing Team of Ghost Pokémon ---
print("\n[2] Summoning an opposing Ghost-type Pokémon team from PokéAPI...")
# Let's pick 3 iconic Ghost Pokémon to match our cross-over battle
ghost_team = ["gengar", "chandelure", "mimikyu"]
pokemon_roster = []

for poke_name in ghost_team:
    poke_res = requests.get(f"{POKE_URL}pokemon/{poke_name}")
    if poke_res.status_code == 200:
        poke_data = poke_res.json()
        pokemon_roster.append({
            "name": poke_data["name"].capitalize(),
            "id": poke_data["id"],
            "types": [t["type"]["name"].capitalize() for t in poke_data["types"]],
            "ability": poke_data["abilities"][0]["ability"]["name"].capitalize()
        })
        print(f"   • Summoned: {poke_data['name'].capitalize()} (#ID: {poke_data['id']}) | Type: Ghost")

print("\n" + "=" * 50)
print("COMBINED SHOWDOWN DATA READY")
print("=" * 50)