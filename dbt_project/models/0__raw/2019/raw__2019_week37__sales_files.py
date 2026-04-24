import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "10cQ3OJ_UdPiZHLTf_-NSEEtV3yc7Gp9w"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
