import openapi_client
from openapi_client import ApiClient, Configuration
from openapi_client.api import studies_api
from config import API_BASE_URL, QUERY_TERM, PAGE_SIZE

def fetch_study_data():

    configuration = Configuration(host=API_BASE_URL)
    api_client = ApiClient(configuration)
    api_instance = studies_api.StudiesApi(api_client)

    raw_study_data = []
    page_token = None

    try:
        while True:
            response = api_instance.list_studies(
                fields=["ProtocolSection"],
                query_term=QUERY_TERM,
                format="json",
                page_token=page_token,
                page_size=PAGE_SIZE
            )

            raw_study_data.extend(response.studies)
            page_token = response.next_page_token
            if not page_token:
                break

    except Exception as e:
        print("Error fetching data:", e)

    return raw_study_data
