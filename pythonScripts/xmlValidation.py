import xml.etree.ElementTree as ET
import requests
import os

# Validate XML structure from a file
def validate_xml_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    try:
        with open(file_path, "r") as file:
            xml_content = file.read()
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"❌ XML Parsing Error in {file_path}: {e}")
        return

    print(f"✅ {file_path} is a valid XML file!")

# Validate XML from a URL
def validate_xml_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        ET.fromstring(response.text)  # Just checking if it's well-formed
        print(f"✅ XML from {url} is valid!")
    except (requests.RequestException, ET.ParseError) as e:
        print(f"❌ Error fetching or parsing XML from {url}: {e}")

if __name__ == "__main__":
    # Validate both saved XML files
    validate_xml_file("fixtures/sample1.xml")  # Replace with actual file path
    validate_xml_file("fixtures/invalidSample.xml")  # Validate another XML file

    # Validate XML from a URL
    validate_xml_from_url("https://www.w3schools.com/xml/note.xml")
