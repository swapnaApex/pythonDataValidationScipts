import pytest
from unittest.mock import patch, mock_open
from xml_utils import validate_xml  # Adjust the import based on your project structure

# To run the test multiple times with different inputs
@pytest.mark.parametrize(
    "file_path, file_exists, file_content, expected",
    [
        # Each tuple contains:
        # (file path, whether file exists, file content, expected validation result)

        ("fixtures/sample1.xml", True, "<root><child></child></root>", True),     # Well-formed (valid) XML
        ("fixtures/invalidSample.xml", True, "<root><child></child>", False),     # Malformed XML (missing closing tag)
        ("fixtures/SampleData1.xml", True, "<root><child></child></root>", True), # Another valid XML file
        ("fixtures/sample3.xml", False, "", False)                                 # Simulates a file that doesn't exist
    ],
    ids=[
        "Simple Valid XML",              # Label for the first test case
        "Malformed XML",                # Label for the second test case
        "Valid XML with many data",     # Label for the third test case
        "File does not exist"           # Label for the fourth test case
    ]
)
@patch("os.path.exists")                        # Mock 'os.path.exists' to simulate file presence
@patch("builtins.open", new_callable=mock_open) # Mock built-in 'open' to simulate reading file contents
def test_validate_xml_file(mock_file, mock_exists, file_path, file_exists, file_content, expected):
    # Mock the result of os.path.exists to return True or False based on the test case
    mock_exists.return_value = file_exists

    # If the file is supposed to exist, mock the file's content to be returned when read
    if file_exists:
        mock_file.return_value.read.return_value = file_content

    # Call the function under test with the mock setup
    result = validate_xml(file_path)

    # Assert the result matches the expected outcome
    assert result == expected
