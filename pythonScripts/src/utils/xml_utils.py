import os
import xml.etree.ElementTree as ET
from utils.logger_utils import setup_logger

# Initialize logger
logger = setup_logger()

def validate_xml(input_data: str, source_name: str = "input string") -> bool:
    """
    Validates whether the input is a well-formed XML string or a valid XML file path.

    Args:
        input_data (str): XML content as a string or a path to an XML file.
        source_name (str): Optional name or description of the source (e.g. filename or Excel row ID)

    Returns:
        bool: True if the XML is well-formed, False otherwise.
    """
    if os.path.exists(input_data) and os.path.isfile(input_data):
        source_name = os.path.basename(input_data)
        try:
            with open(input_data, 'r', encoding='utf-8') as f:
                input_data = f.read()
            logger.info(f"📄 Successfully read XML from file: '{source_name}'")
        except Exception as e:
            logger.error(f"❌ Failed to read file '{source_name}': {e}")
            return False

    # Validate XML string content
    try:
        ET.fromstring(input_data)
        logger.info(f"✅ XML is well-formed (source: {source_name})")
        return True
    except ET.ParseError as e:
        lineno, column = e.position
        logger.error(f"❌ XML not well-formed (source: {source_name}): {e.msg}")
        logger.debug(f"XML Error in {source_name} at line {lineno}, column {column}")
        return False
