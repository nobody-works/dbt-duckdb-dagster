import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "1Rzx-P8o9Xel6H_bF2HziLCXsyabUWqAM"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
