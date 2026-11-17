# Databricks notebook source
# MAGIC %md
# MAGIC # Revisar antes del commit
# MAGIC
# MAGIC Córrelo completo (**Run all**) antes de cada commit. Hace en Databricks lo que en
# MAGIC una PC de desarrollo hacen `uv sync`, `uv run pytest` y el guardia de pre-commit:
# MAGIC
# MAGIC 1. Instala el paquete y sus herramientas, según `pyproject.toml`.
# MAGIC 2. Corre las pruebas.
# MAGIC 3. Pasa el guardia: ruff arregla el formato y revisa las reglas.
# MAGIC
# MAGIC Si una celda falla, lee su mensaje, corrige y vuelve a correr todo.

# COMMAND ----------

# MAGIC %pip install --quiet -e "..[dev]"

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

import os
import subprocess
import sys


def ejecutar(*comando: str) -> int:
    """Corre una herramienta en la raíz del repositorio y muestra lo que responde."""
    resultado = subprocess.run(
        [sys.executable, "-m", *comando],
        cwd="..",
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    print(resultado.stdout, resultado.stderr)
    return resultado.returncode


# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Las pruebas

# COMMAND ----------

codigo = ejecutar("pytest", "-p", "no:cacheprovider")
assert codigo == 0, "Alguna prueba falló: lee el mensaje de arriba."

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. El guardia: formato y reglas
# MAGIC
# MAGIC `ruff check` revisa las reglas y arregla lo que puede; lo que no, te lo dice con
# MAGIC su código (por ejemplo, `ANN001`). `ruff format` acomoda el estilo por ti.
# MAGIC Revisa el paquete y las pruebas; los notebooks quedan fuera (ver `pyproject.toml`).

# COMMAND ----------

codigo = ejecutar("ruff", "check", "--fix", "--no-cache", ".")
ejecutar("ruff", "format", "--no-cache", ".")
assert codigo == 0, "ruff encontró problemas: lee el mensaje de arriba."

# COMMAND ----------

# MAGIC %md
# MAGIC Si llegaste hasta aquí sin errores, ya puedes hacer el commit.
