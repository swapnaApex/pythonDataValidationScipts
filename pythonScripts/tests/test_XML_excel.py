import pytest
import os
import pandas as pd
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))
from utils.xml_utils import validate_xml

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
FIXTURE_PATH = os.path.join(PROJECT_ROOT, "fixtures", "testcases_inputs.xlsx")

def load_test_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    test_cases = [(row['xml_content'], row['expected_result']) for _, row in df.iterrows()]
    return test_cases

# Parametrize test function using data from Excel
@pytest.mark.parametrize(
    "xml_content, expected_result",  # Parameters must match the ones used in the test function
    load_test_data_from_excel(FIXTURE_PATH) # Excel file has 'xml_content' and 'expected_result'
)
def test_xml_content_direct(xml_content, expected_result):
    # Assert the XML validation result matches the expected result
    assert validate_xml(xml_content) == expected_result
