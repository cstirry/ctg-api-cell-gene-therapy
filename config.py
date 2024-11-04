from datetime import datetime, timedelta

# Configuration file for API settings
API_BASE_URL = "https://clinicaltrials.gov/api/v2"
PAGE_SIZE = 1000

# Set the date range
#START_DATE = "2024-01-01"
#END_DATE = "2024-12-31"
END_DATE = datetime.now().strftime("%Y-%m-%d") # Calculate START_DATE as one week ago and END_DATE as today
START_DATE = (datetime.now() - timedelta(weeks=1)).strftime("%Y-%m-%d")

# Use the QUERY_TERM_TEMPLATE to format the dates
QUERY_TERM_TEMPLATE = "AREA[LastUpdatePostDate]RANGE[{START_DATE},{END_DATE}]"
QUERY_TERM = QUERY_TERM_TEMPLATE.format(START_DATE=START_DATE, END_DATE=END_DATE)

# Configuration for outputs
OUTPUT_PATH = "data/"

# Configuration for keyword match
CELL_GENE_THERAPY_TERMS = [
    "car t-cell", "car-t", "chimeric antigen receptor", "natural killer cell", "nk cell",
    " til ", "tumor-infiltrating lymphocytes", "adoptive cell transfer", "cell therapy",
    "cell transfer", "somatic cell therapy", "modified cell",
    "hematopoietic stem cell transplantation", " hsc ", "mesenchymal stem cell",
    "induced pluripotent stem cell", " ipsc ", "embryonic stem cell",
    "bone marrow transplant", "umbilical cord blood",  "gene therapy", "gene transfer",
    "gene editing", "gene modif", "gene-modif", "genetically engineer",
    "genetically modif", "genetic modif", "crispr", "zinc finger nuclease",
    "adenoviral", "lentiviral", "retroviral", "oncolytic virus", "viral vector",
    "non-viral vector", " aav ", "adeno-associated virus", "immunotherapy",
    "allogeneic", "autologous", "in vivo", "ex vivo",  "cell seed", "scaffold"
]
