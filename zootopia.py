import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def print_animal_info(data):
    """Function to extract and print the data for each animal"""
    for animal in animals_data:
        name = animal.get("name", "Unknown")
        locations = ", ".join(animal.get("locations", []))
        characteristics = animal.get("characteristics", {})
        common_name = characteristics.get("common_name", "Unknown")
        diet = characteristics.get("diet", "Unknown")
        lifespan = characteristics.get("lifespan", "Unknown")

        print(f"Name: {name}")
        print(f"Common Name: {common_name}")
        print(f"Locations: {locations}")
        print(f"Diet: {diet}")
        print(f"Lifespan: {lifespan}")
        print("-" * 40)

# Aufrufen der Funktion
print_animal_info(animals_data)