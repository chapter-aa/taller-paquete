"""Funciones de limpieza del dataset Hotel Booking."""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df


def add_arrival_month(df: pd.DataFrame) -> pd.DataFrame:
    # Corregir la fecha 2018-2-29, convertirla a fecha, sumar el lead_time y sacar el mes.
    df = df.copy()
    df["date_of_reservation"] = df["date_of_reservation"].astype(str)
    df["date_of_reservation"] = df["date_of_reservation"].replace(
        "2018-2-29", "03/01/2018"
    )

    reservation_date = pd.to_datetime(df["date_of_reservation"], format="%m/%d/%Y")
    arrival_date = reservation_date + pd.to_timedelta(df["lead_time"], unit="days")
    df["arrival_month"] = arrival_date.dt.month

    return df
