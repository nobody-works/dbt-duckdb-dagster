import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "11fD8DMPzhch5Bu0bqeRiOuRHgFrNq1Dn0pqI7uEKUDc"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
