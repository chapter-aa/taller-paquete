"""Preprocesa las reservas con el paquete hotel_booking.

Lo corre el job del bundle (resources/preprocesamiento.yml). Es el notebook
preprocesamiento.py, pero usando las funciones del paquete y la configuración.
"""

import argparse

import pandas as pd

from hotel_booking.config import ProjectConfig
from hotel_booking.preprocessing import (
    add_arrival_month,
    add_total_nights,
    clean_column_names,
)

parser = argparse.ArgumentParser()
parser.add_argument("--config_path", required=True)
parser.add_argument("--env", default="dev")
args = parser.parse_args()

config = ProjectConfig.from_yaml(args.config_path, env=args.env)
ruta = f"/Volumes/{config.catalog}/{config.schema_name}/datos/booking.csv"

df = pd.read_csv(ruta)
df = clean_column_names(df)
df = add_total_nights(df)
df = add_arrival_month(df)

print(f"Entorno {args.env}: {len(df):,} reservas leídas de {ruta}")
print("Reservas por mes de llegada:")
print(df["arrival_month"].value_counts().sort_index().to_string())
print("Primeras filas:")
print(df[["date_of_reservation", "lead_time", "arrival_month", "total_nights"]].head())
