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

def check_required_elements(xml_str: str, required_elements: List[str], source_name: str = "input string") -> bool:
    #function to validate the elements of XML has the specific elements
    try:
        root = ET.fromstring(xml_str)
        missing_elements = []
        for elem in required_elements:
            found = root.find(elem)
            if found is None:
                missing_elements.append(elem)

        if missing_elements:
            logger.warning(f"⚠️ Missing required elements in '{source_name}': {missing_elements}")
            return False

        logger.info(f"✅ All required elements found in '{source_name}'")
        return True
    except ET.ParseError as e:
        logger.error(f"❌ Invalid XML content in '{source_name}': {e}")
        return False


def validate_element_data_types(xml_str: str, element_types: Dict[str, type], source_name: str = "input string") -> bool:
    #function checks whether the XML tag have specific data types as per requirement
    try:
        root = ET.fromstring(xml_str)
        errors = []
        for tag, expected_type in element_types.items():
            element = root.find(tag)
            if element is not None and element.text is not None:
                try:
                    expected_type(element.text) 
                except ValueError:
                    errors.append(f"{tag} should be {expected_type.__name__}, got '{element.text}'")
            else:
                errors.append(f"{tag} not found or empty")

        if errors:
            logger.warning(f"⚠️ Type validation issues in '{source_name}': {errors}")
            return False

        logger.info(f"✅ Element types validated for '{source_name}'")
        return True
    except ET.ParseError as e:
        logger.error(f"❌ Invalid XML content in '{source_name}': {e}")
        return False
