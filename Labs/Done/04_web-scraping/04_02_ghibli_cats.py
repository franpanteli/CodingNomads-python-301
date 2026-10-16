# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

# 1. Fetch the species list to locate the "Cat" species and its character links
species_response = requests.get(f"{BASE_URL}/species")
species_list = species_response.json()

cat_character_urls = []
for species in species_list:
  if species.get("name", "").lower() == "cat":
    cat_character_urls = species.get("people", [])
    break

# 2. Fetch and print details for each cat character
print("Studio Ghibli Cats Found:\n")
for url in cat_character_urls:
  # Extract the character ID to ensure we query the active base URL
  char_id = url.split("/")[-1]
  char_response = requests.get(f"{BASE_URL}/people/{char_id}")
  cat = char_response.json()

  print(f"Name: {cat.get('name')}")
  print(f"  - Gender: {cat.get('gender')}")
  print(f"  - Eye Color: {cat.get('eye_color')}")
  print(f"  - Hair Color: {cat.get('hair_color')}\n")