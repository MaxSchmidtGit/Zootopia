import data_fetcher

def serialize_animal(animal_obj):
    """Serialize a single animal object to HTML."""
    output = '<li class="cards__item"><div class="card"><div class="card__content">'
    name = animal_obj.get("name")
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    if name:
        output += f"<p><strong>Name:</strong> {name}</p>\n"
    for key, value in characteristics.items():
        output += f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>\n"
    if locations:
        output += f"<p><strong>Location:</strong> {locations[0]}</p>\n"
    output += '</div></div></li>\n'  # Close the card and list item
    return output

def generate_animal_info(animals_data, animal_name):
    """Generate a string with the animals' data in HTML format."""
    if not animals_data:
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output

def replace_placeholder(template_path, output_path, placeholder, replacement):
    """Replace the placeholder in the HTML template and write to a new file."""
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    new_content = template_content.replace(placeholder, replacement)

    with open(output_path, "w") as output_file:
        output_file.write(new_content)

def main():
    animal_name = input("Please enter an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)
    animal_info = generate_animal_info(animals_data, animal_name)
    replace_placeholder('animals_template.html', 'animals.html', '__REPLACE_ANIMALS_INFO__', animal_info)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()
