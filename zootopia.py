import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def print_animal_info(animals_data):
    """Function to extract and print the data for each animal"""
    for animal in animals_data:
        name = animal.get("name", "Unknown")
        locations = ", ".join(animal.get("locations", []))
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        animal_type = characteristics.get("type", "Unknown")

        print(f"Name: {name}")
        print(f"Location: {locations}")
        print(f"Diet: {diet}")
        print(f"Type: {animal_type}")
        print("-" * 40)
        print(f"DEBUG: Characteristics for {name}: {characteristics}")
# Aufrufen der Funktion
print_animal_info(animals_data)