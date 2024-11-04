import os
import pandas as pd
from src.api_client import fetch_study_data
from src.fetch_data import process_study_data
from src.utils import unwrap_single_element, filter_cell_gene_therapy_studies
from config import OUTPUT_PATH, START_DATE, END_DATE


def main():
    # Fetch and process data from the API
    print("Running data pipeline...")
    raw_data = fetch_study_data()
    processed_df = process_study_data(raw_data)

    print("Filtering for cell and gene therapy studies...")
    filtered_df = filter_cell_gene_therapy_studies(processed_df)

    # Create additional DataFrames for collaborator and location data because 1:many
    print("Creating collaborator and location dataframes...")
    collaborator_df = filtered_df[['nct_id', 'sponsor', 'collaborators']].explode('collaborators')
    location_df = filtered_df[['nct_id', 'location_facility', 'country', 'geo_point']].explode(
        ['location_facility', 'country', 'geo_point'])

    print("Extra processing...")
    filtered_df = filtered_df.applymap(unwrap_single_element)

    # Save the DataFrames to CSV files
    filtered_df.to_csv(f"{OUTPUT_PATH}/data_{START_DATE}_{END_DATE}.csv", index=False)
    collaborator_df.to_csv(f"{OUTPUT_PATH}/collaborator_{START_DATE}_{END_DATE}.csv", index=False)
    location_df.to_csv(f"{OUTPUT_PATH}/location_{START_DATE}_{END_DATE}.csv", index=False)

    print("Data pipeline completed successfully.")


if __name__ == "__main__":

    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    main()
