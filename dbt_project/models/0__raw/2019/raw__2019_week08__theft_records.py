import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "1U0hPPU9zzI1tJYaAF29Uva-3NaH04l07"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
