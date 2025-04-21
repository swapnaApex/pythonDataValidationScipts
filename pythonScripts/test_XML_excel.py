
import pytest
from unittest.mock import patch
import pytest
import pandas as pd
from xml_utils import is_well_formed  # Adjust the import based on your project structure

def load_test_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    test_cases = [(row['xml_content'], row['expected_result']) for _, row in df.iterrows()]
    return test_cases

# Parametrize test function using data from Excel
@pytest.mark.parametrize(
    "xml_content, expected_result",  # Parameters must match the ones used in the test function
    load_test_data_from_excel("fixtures/testcases_inputs.xlsx")  # Assuming your Excel file has 'xml_content' and 'expected_result'
)
def test_xml_content_direct(xml_content, expected_result):
    # Assert the XML validation result matches the expected result
    assert is_well_formed(xml_content) == expected_result
