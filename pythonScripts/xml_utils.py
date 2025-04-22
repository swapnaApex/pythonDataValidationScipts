import os
import sys
import xml.etree.ElementTree as ET  # Built-in library to parse and validate XML

def validate_xml(input_data: str) -> bool:
    """
    Validates whether the input is a well-formed XML string or a valid XML file path.

    Args:
        input_data (str): XML content as a string or a path to an XML file.

    Returns:
        bool: True if the XML is well-formed, False otherwise.
    """
    # Check if input is a path to a file
    if os.path.exists(input_data) and os.path.isfile(input_data):
        try:
            with open(input_data, 'r', encoding='utf-8') as f:
                input_data = f.read()  # Read file contents into string
        except Exception as e:
            print(f"❌ Failed to read file: {e}")
            return False

    try:
        ET.fromstring(input_data)
        return True
    except ET.ParseError as e:
        print(f"❌ XML is not well-formed: {e}")
        return False
    
def main():
    # Check if exactly one argument (the XML file path) was provided
    if len(sys.argv) != 2:
        print("Usage: python xml_utils.py <file_path>")
        sys.exit(1)

    # Get the file path from the command-line argument
    file_path = sys.argv[1]

    # Validate the XML file and print the result
    if validate_xml(file_path):
        print("Valid XML.")
    else:
        print("Invalid XML.")

# Trigger the main function only when running this script directly
if __name__ == "__main__":
    main()
