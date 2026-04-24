import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "16OFZwSyA2FvSfUnoybdg12bSzlUy8J0i"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
