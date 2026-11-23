"""Funciones de limpieza del dataset Hotel Booking."""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df


def add_arrival_month(df):
    df = df.copy()

    # Convierte a fecha. Las fechas inválidas quedan como NaT
    df["date_of_reservation"] = pd.to_datetime(
        df["date_of_reservation"],
        errors="coerce"
    )

    # Corrección específica para la fecha inválida 2018-2-29
    mask = (
        df["date_of_reservation"].isna() &
        (df["lead_time"] == 0)
    )

    df.loc[mask, "date_of_reservation"] = pd.Timestamp("2018-03-01")

    # Fecha de llegada
    df["arrival_date"] = (
        df["date_of_reservation"] +
        pd.to_timedelta(df["lead_time"], unit="D")
    )

    # Mes de llegada
    df["arrival_month"] = df["arrival_date"].dt.month

    return df