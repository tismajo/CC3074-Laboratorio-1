import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# El archivo está separado por comas.
# Algunas columnas contienen listas internas separadas por '|',
# pero esto no afecta el delimitador principal del CSV.

df = pd.read_csv("movies_2026.csv", sep=",", encoding="latin1")

# 1. Haga una exploración rápida de sus datos, para eso haga un resumen de su conjunto de datos.
# 19883 filas y 28 columnas
""" columnsAndRows = df.shape
print(columnsAndRows) """

# Nombres de las variables
""" varName = df.columns
print(varName)
"""

# Vista rápida de los datos
""" viewData = df.head()
print(viewData) """

# Tipos de los datos (int, float, str...), 2. Diga el tipo de cada una de las variables (cualitativa ordinal o nominal, cuantitativa continua, cuantitativa discreta)
""" inferredData = df.dtypes
print(inferredData) """

# Resumen estadístico
""" statisticalSummary = df.describe()
print(statisticalSummary) """

# Valores faltantes, se detectan datos faltantes.
""" missingValues = df.isna().sum().sort_values(ascending=False)
print(missingValues) """

# 3. Investigue si las variables cuantitativas siguen una distribución normal y haga una tabla de frecuencias de las variables cualitativas. Explique todos los resultados.
quantitativeVars = [
    "budget", "revenue", "runtime", "popularity",
    "voteAvg", "voteCount", "genresAmount",
    "productionCoAmount", "productionCountriesAmount",
    "actorsAmount", "castWomenAmount", "castMenAmount",
    "releaseYear"
]

multiValueQualitativeVars = [
    "genres",
    "productionCountry",
    "productionCompanyCountry",
    "actorsCharacter"
]

simpleQualitativeVars = [
    "originalLanguage",
    "video",
    "director"
]

# Histogramas
""" for var in quantitativeVars:
    plt.figure(figsize=(6,4))
    sns.histplot(df[var], bins=50, kde=True)
    plt.title(f"Distribución de {var}")
    plt.xlabel(var)
    plt.ylabel("Frecuencia")
    plt.show() """

# Prueba de normalidad
""" for var in quantitativeVars:
    data = df[var].dropna()
    stat, p = stats.kstest(
        (data - data.mean()) / data.std(),
        'norm'
    )
    print(f"{var}: estadístico={stat:.4f}, p-valor={p:.4f}") """

# Tablas de frecuencias - variables cualitativas
frequencyTables = {}

# Valores simples
for var in simpleQualitativeVars:
    freqAbs = df[var].value_counts(dropna=False)
    freqRel = df[var].value_counts(normalize=True, dropna=False) * 100

    freqTable = pd.DataFrame({
        "Frecuencia absoluta": freqAbs,
        "Frecuencia relativa (%)": freqRel.round(2)
    })

    frequencyTables[var] = freqTable

    print(f"\nTabla de frecuencias: {var}")
    print(freqTable.head(10))

# Valores multivariables
""" for var in multiValueQualitativeVars:
    exploded = (
        df[var]
        .dropna()
        .astype(str)
        .str.split("|")
        .explode()
        .str.strip()
    )

    freqAbs = exploded.value_counts()
    freqRel = exploded.value_counts(normalize=True) * 100

    freqTable = pd.DataFrame({
        "Frecuencia absoluta": freqAbs,
        "Frecuencia relativa (%)": freqRel.round(2)
    })

    frequencyTables[var] = freqTable

    print(f"\nTabla de frecuencias (separado por '|'): {var}")
    print(freqTable.head(10)) """
