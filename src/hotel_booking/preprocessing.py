"""Funciones de limpieza del dataset Hotel Booking."""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza espacios y guiones de los nombres de columna por guiones bajos."""
    df = df.copy()
    df.columns = df.columns.str.replace(r"[ -]", "_", regex=True)
    return df

def add_arrival_month(df: pd.DataFrame) -> pd.DataFrame:
    """Corrige la fecha imposible 2018-2-29 (2018 no fue bisiesto), calcula la
    fecha de llegada sumando los días de anticipación y agrega el mes de arribo."""
    texto = df["date_of_reservation"].astype(str)
    texto = texto.where(texto != "2018-2-29", "3/1/2018")
    llegadas = pd.to_datetime(texto, format="%m/%d/%Y") + pd.to_timedelta(
        df["lead_time"], unit="D"
    )
    return df.assign(
        date_of_reservation=texto,
        date_of_arrival=llegadas,
        arrival_month=llegadas.dt.month,
    )
    


