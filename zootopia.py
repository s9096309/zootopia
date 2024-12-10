import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animals_html(data):
    """Generates the HTML content for the animals' data."""
    animals_html = ""
    for animal in data:
        name = animal.get("name", "Unknown")
        locations = ", ".join(animal.get("locations", []))
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        type_value = characteristics.get("type", "Unknown")

        animals_html += f"""
        <li class="cards__item">
            Name: {name}<br/>
            Diet: {diet}<br/>
            Location: {locations or "Unknown"}<br/>
            Type: {type_value}<br/>
        </li>
        """
    return animals_html

def generate_html(template_path, output_path, animals_data):
    """Generates a new HTML file by replacing a placeholder in the template."""
    # Read the HTML template
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    # Generate the animals HTML
    animals_html = generate_animals_html(animals_data)

    # Replace the placeholder with the generated animals' HTML
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write the final HTML content to a new file
    with open(output_path, "w") as output_file:
        output_file.write(final_html)

# Paths to the files
template_path = "animals_template.html"
output_path = "animals.html"
json_path = "animals_data.json"

# Load data and generate the HTML
animals_data = load_data(json_path)
generate_html(template_path, output_path, animals_data)

print(f"HTML file has been generated: {output_path}")
