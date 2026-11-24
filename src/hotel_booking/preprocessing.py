"""Funciones de limpieza del dataset Hotel Booking."""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df


def add_total_nights(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula el número total de noches de una reserva."""
    df = df.copy()
    df["total_nights"] = df["number_of_weekend_nights"] + df["number_of_week_nights"]
    return df


def add_arrival_month(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la fecha y el mes de llegada a partir de la reserva y el lead time."""
    df = df.copy()
    df["date_of_reservation"] = df["date_of_reservation"].replace("2018-2-29", "3/1/2018")
    df["date_of_reservation"] = pd.to_datetime(
        df["date_of_reservation"], format="%m/%d/%Y"
    )
    df["arrival_date"] = df["date_of_reservation"] + pd.to_timedelta(
        df["lead_time"], unit="d"
    )
    df["arrival_month"] = df["arrival_date"].dt.month
    return df
