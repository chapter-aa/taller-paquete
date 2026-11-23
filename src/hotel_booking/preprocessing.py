"""Funciones de limpieza del dataset Hotel Booking."""

from datetime import datetime

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df


def add_arrival_month(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date_of_reservation"] = df["date_of_reservation"].apply(
        lambda x: "3/1/2018" if x == "2018-2-29" else x
    )
    df["date_of_reservation"] = df["date_of_reservation"].apply(
        lambda x: datetime.strptime(x, "%m/%d/%Y")
    )
    df["arrival_date"] = df["date_of_reservation"] + pd.to_timedelta(
        df["lead_time"], unit="d"
    )
    df["arrival_month"] = df["arrival_date"].dt.month
    return df
