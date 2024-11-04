from config import CELL_GENE_THERAPY_TERMS


def unwrap_single_element(value):
    if isinstance(value, list) and len(value) == 1:
        return value[0]
    return value


def find_matching_terms(row):
    text = f"{row['official_title']} {row['brief_summary']}".lower()
    matching_terms = [term for term in CELL_GENE_THERAPY_TERMS if term in text]
    return ", ".join(matching_terms) if matching_terms else None


def filter_cell_gene_therapy_studies(df):
    # Apply the function to create the `matching_terms` column
    df['matching_terms'] = df.apply(find_matching_terms, axis=1)

    # Create a column to flag cell and gene therapy based on the presence of matching terms
    df['is_cell_gene_therapy'] = df['matching_terms'].notnull()

    return df[df['is_cell_gene_therapy']]
