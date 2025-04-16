import os
import sys
import xml.etree.ElementTree as ET  # Built-in library to parse and validate XML

def validate_xml_file(file_path: str) -> bool:
    """
    Validates whether the given XML file exists and is well-formed.
    
    Args:
        file_path (str): The path to the XML file.
        
    Returns:
        bool: True if the file exists and is valid XML, False otherwise.
    """

    # Check if the file actually exists on the filesystem
    if not os.path.exists(file_path):
        return False

    try:
        # Open the file and read its contents
        with open(file_path, 'r') as f:
            content = f.read()

            # Try to parse the XML string; will raise ET.ParseError if malformed
            ET.fromstring(content)

        # If no exception is raised, the XML is valid
        return True

    except ET.ParseError:
        # Raised when the XML is not well-formed
        return False


# This part only runs when the script is executed directly (not imported)
def main():
    # Check if exactly one argument (the XML file path) was provided
    if len(sys.argv) != 2:
        print("Usage: python xml_utils.py <file_path>")
        sys.exit(1)

    # Get the file path from the command-line argument
    file_path = sys.argv[1]

    # Validate the XML file and print the result
    if validate_xml_file(file_path):
        print("Valid XML.")
    else:
        print("Invalid XML.")

# Trigger the main function only when running this script directly
if __name__ == "__main__":
    main()
