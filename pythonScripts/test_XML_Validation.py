import os
import xml.etree.ElementTree as ET
import requests
from unittest.mock import patch, mock_open
import pytest

# Function to be tested
def validate_xml_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        with open(file_path, "r") as file:
            xml_content = file.read()
        ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"❌ XML Parsing Error in {file_path}: {e}")
        return False

    print(f"✅ {file_path} is a valid XML file!")
    return True

def validate_xml_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        ET.fromstring(response.text)  # Just checking if it's well-formed
        print(f"✅ XML from {url} is valid!")
        return True
    except (requests.RequestException, ET.ParseError) as e:
        print(f"❌ Error fetching or parsing XML from {url}: {e}")
        return False

# Pytest test cases
@pytest.mark.parametrize("file_path, file_exists, file_content, expected", [
    ("fixtures/sample1.xml", True, "<root><child></child></root>", True),  # ✅ Valid XML
    ("fixtures/invalidSample.xml", True, "<root><child></child>", False),  # ❌ Malformed XML
    ("fixtures/sample3.xml", False, "", False)  # ❌ File does not exist
])
@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_validate_xml_file(mock_file, mock_exists, file_path, file_exists, file_content, expected):
    mock_exists.return_value = file_exists
    mock_file.return_value.read.return_value = file_content

    result = validate_xml_file(file_path)

    assert result == expected