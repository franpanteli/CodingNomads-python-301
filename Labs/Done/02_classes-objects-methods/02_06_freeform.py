# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

# --- Class 1: CoffeeCup ---
class CoffeeCup:
    def __init__(self, blend, size, shots):
        self.blend = blend
        self.size = size        # e.g., "Small", "Medium", "Large"
        self.shots = shots      # Number of espresso shots

    def __str__(self):
        return f"{self.size} {self.blend} Coffee with {self.shots} espresso shot(s)."


# --- Class 2: Playlist (Overloading __add__) ---
class Playlist:
    def __init__(self, title, genre, song_count):
        self.title = title
        self.genre = genre
        self.song_count = song_count

    def __str__(self):
        return f"Playlist: '{self.title}' [{self.genre}] — {self.song_count} songs"

    # Overloading the '+' operator to combine two playlists
    def __add__(self, other):
        if isinstance(other, Playlist):
            new_title = f"{self.title} + {other.title}"
            new_genre = f"{self.genre} & {other.genre}"
            new_song_count = self.song_count + other.song_count
            return Playlist(new_title, new_genre, new_song_count)
        return NotImplemented


# --- Class 3: Houseplant ---
class Houseplant:
    def __init__(self, species, height_cm, is_thirsty):
        self.species = species
        self.height_cm = height_cm
        self.is_thirsty = is_thirsty

    def __str__(self):
        status = "thirsty 🥀" if self.is_thirsty else "hydrated & thriving 🌿"
        return f"{self.species} | Height: {self.height_cm}cm | Status: {status}"


# ==========================================
# TESTING THE CLASSES
# ==========================================

print("=== 1. COFFEE SHOP ORDER ===")
cup1 = CoffeeCup("Dark Roast", "Medium", 2)
cup2 = CoffeeCup("Vanilla Latte", "Large", 1)

print("Before modification:")
print(cup1)
print(cup2)

# Modifying attributes
cup1.size = "Large"
cup1.shots = 3

print("\nAfter modification (Upgraded Cup 1):")
print(cup1)


print("\n=== 2. MUSIC PLAYLISTS (Adding with '+') ===")
playlist1 = Playlist("Coding Focus", "Lo-Fi", 45)
playlist2 = Playlist("Late Night Beats", "Synthwave", 30)

print(playlist1)
print(playlist2)

# Using the overloaded '+' operator
mega_playlist = playlist1 + playlist2
print("\nCombined via '+' operator:")
print(mega_playlist)

# Modifying an attribute
playlist1.song_count = 50
print(f"Updated '{playlist1.title}' song count: {playlist1.song_count} songs")


print("\n=== 3. HOUSEPLANTS ===")
plant1 = Houseplant("Monstera Deliciosa", 60, True)
plant2 = Houseplant("Snake Plant", 40, False)

print("Before watering/growth:")
print(plant1)
print(plant2)

# Modifying attributes (watering plant1 and growing plant2)
plant1.is_thirsty = False
plant2.height_cm = 45

print("\nAfter care update:")
print(plant1)
print(plant2)