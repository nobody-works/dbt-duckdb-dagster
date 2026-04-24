import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "159kPOITI2sNf9EvkHkIdVOMmP6_dDN5o"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
