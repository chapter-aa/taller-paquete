"""Funciones de limpieza del dataset Hotel Booking."""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df


def add_arrival_month(df: pd.DataFrame) -> pd.DataFrame:
    """Corrige la fecha 2018-2-29, la convierte a fecha,
    le suma el lead_time y saca el mes de arribo"""
    df = df.copy()
    df["date_of_reservation"] = (
        df["date_of_reservation"].astype(str).str.replace("2018-2-29", "3/1/2018")
    )
    df["date_of_arrival"] = pd.to_datetime(
        df["date_of_reservation"], format="%m/%d/%Y"
    ) + pd.to_timedelta(df["lead_time"], unit="d")
    df["arrival_month"] = df["date_of_arrival"].dt.month
    return df
