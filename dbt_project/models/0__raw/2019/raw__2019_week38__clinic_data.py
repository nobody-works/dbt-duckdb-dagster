import polars as pl


def model(dbt, session):
    dbt.config(materialized="table")

    file_id = "12ei7St-tC2sf6ongm570P2U4UCqSDBg4"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    df = pl.read_csv(url)
    return df.to_pandas()
