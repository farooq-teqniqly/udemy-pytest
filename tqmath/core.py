import pandas as pd


def dict_to_dataframe(d: dict) -> pd.DataFrame:
    if d is None:
        raise ValueError("Input dictionary not specified.")

    return pd.DataFrame([d])
