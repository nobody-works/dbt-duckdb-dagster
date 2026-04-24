import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "1UljNZ3oB3j9GFy4S3UkMXae1CgjlZaou"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
