import pytest
from unittest.mock import patch, mock_open
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))
from utils.xml_utils import validate_xml

# To run the test multiple times with different inputs
@pytest.mark.parametrize(
    "file_path, file_exists, file_content, expected",
    [
        ("fixtures/sample1.xml", True, "<root><child></child></root>", True),     # Well-formed XML
        ("fixtures/invalidSample.xml", True, "<root><child></child>", False),     # Malformed XML
        ("fixtures/SampleData1.xml", True, "<root><child></child></root>", True), # Another valid XML
        ("fixtures/sample3.xml", False, "", False)                                # File does not exist
    ],
    ids=["Simple Valid XML", "Malformed XML", "Valid XML with many data", "File does not exist"]
)
@patch("os.path.exists")  # Mock os.path.exists to simulate file presence
@patch("builtins.open", new_callable=mock_open)  # Mock open to simulate file reading
def test_validate_xml_file(mock_file, mock_exists, file_path, file_exists, file_content, expected):
    # Mock os.path.exists return value
    mock_exists.return_value = file_exists
    
    # If the file is supposed to exist, mock the file's content
    if file_exists:
        mock_file.return_value.read.return_value = file_content  # Mock reading file content
    
    # Call the function under test with the mock setup
    result = validate_xml(file_path)
    
    # Assert that the result matches the expected outcome
    assert result == expected