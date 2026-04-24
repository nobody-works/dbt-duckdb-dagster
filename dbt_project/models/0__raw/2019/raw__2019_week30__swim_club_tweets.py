import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "1-u64xX2w7O2Zy5dtDo6pNOW8NC7cAsZb"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
