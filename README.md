# Clinical Trials Data Pipeline

This repository contains a Python data pipeline that uses the ClinicalTrials.gov API to 
retrieve clinical trial study data by date range, filters for cell and gene therapy studies, 
and outputs results as CSV files used in a [Tableau Public dashboard.](https://public.tableau.com/app/profile/christine.stirrat/viz/ctg-cell-gene-therapy-orgs/Dashboard)

## Installation

This project uses an API client generated from the ClinicalTrials.gov OpenAPI specification.

1. Clone the repository

2. Download the YAML file from ClinicalTrials.gov. See https://clinicaltrials.gov/data-api/api

3. Download the OpenAPI Generator JAR. See https://openapi-generator.tech/docs/installation for additional options. Requires Java.

4. Generate the OpenAPI Python client. Example:
   ```bash
   java -jar openapi-generator-cli.jar generate -i ctg-oas-v2.yaml -g python -o generated-client
   ```

5. Install dependencies. Pipeline expects the generated-client folder with the openapi_client.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update `config.py` with preferred date range if necessary. The default is the past week of studies.

2. Run the main script to execute the pipeline:
   ```bash
   python main.py
   ```

3. The output CSV files will be saved in the `data/` directory.

## Additional features

The pipeline uses pytest for testing, GitHub Actions for CI/CD, 
and Pydantic for data validation.

## License

This project is licensed under the [MIT License](LICENSE).