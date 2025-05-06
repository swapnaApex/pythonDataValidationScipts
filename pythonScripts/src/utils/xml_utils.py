import os
import xml.etree.ElementTree as ET
from utils.logger_utils import setup_logger

# Initialize logger
logger = setup_logger()

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
            logger.info(f"📄 Successfully read XML file: {input_data[:50]}...")  # Log first 50 chars for debugging
        except Exception as e:
            logger.error(f"❌ Failed to read file: {e}")
            return False

    # Validate the XML (either string or file content)
    try:
        ET.fromstring(input_data)
        logger.info("✅ XML is well-formed.")
        return True
    except ET.ParseError as e:
        lineno, column = e.position
        logger.error(f"❌ XML is not well-formed: {e.msg}")
        logger.debug(f"XML Error: {e.msg} at line {lineno}, column {column}")
        return False
