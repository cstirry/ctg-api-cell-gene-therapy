import pytest
import pandas as pd
from src.fetch_data import process_study_data


def test_process_study_data():
    # Example raw data for testing
    raw_data = [
        {"protocol_section": {"identification_module": {"nct_id": "NCT12345"}}},
        {"protocol_section": {"identification_module": {"nct_id": "NCT67890"}}}
    ]

    # Process the data
    df = process_study_data(raw_data)

    # Check that the DataFrame is not empty
    assert not df.empty, "DataFrame is empty"

    # Check that the correct columns exist
    assert "nct_id" in df.columns, "'nct_id' column is missing"

    # Check the number of rows
    assert len(df) == 2, "Number of rows in DataFrame is incorrect"
