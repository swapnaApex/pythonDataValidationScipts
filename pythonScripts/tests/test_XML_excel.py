import pytest
import os
import pandas as pd
import sys

# Setup path for importing src module
try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
    from utils.xml_utils import validate_xml
except ImportError as e:
    pytest.fail(f"Import failed: {e}")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
FIXTURE_PATH = os.path.join(PROJECT_ROOT, "fixtures", "testcases_inputs.xlsx")

def load_test_data_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        if not {'xml_content', 'expected_result'}.issubset(df.columns):
            raise ValueError("Excel file must contain 'xml_content' and 'expected_result' columns")
        return [(row['xml_content'], row['expected_result']) for _, row in df.iterrows()]
    except Exception as e:
        pytest.fail(f"Failed to load test data from Excel: {e}")

# Parametrize test function using data from Excel
@pytest.mark.parametrize(
    "xml_content, expected_result",
    load_test_data_from_excel(FIXTURE_PATH)
)
def test_xml_content_direct(xml_content, expected_result):
    assert validate_xml(xml_content) == expected_result
