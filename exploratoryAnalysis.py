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
""" quantitativeVars = [
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
] """

""" simpleQualitativeVars = [
    "originalLanguage",
    "video",
    "director"
] """

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
""" frequencyTables = {}
 """
# Valores simples
""" for var in simpleQualitativeVars:
    freqAbs = df[var].value_counts(dropna=False)
    freqRel = df[var].value_counts(normalize=True, dropna=False) * 100

    freqTable = pd.DataFrame({
        "Frecuencia absoluta": freqAbs,
        "Frecuencia relativa (%)": freqRel.round(2)
    })

    frequencyTables[var] = freqTable

    print(f"\nTabla de frecuencias: {var}")
    print(freqTable.head(10)) """

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

# 4 Responda las siguientes preguntas:
df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")
df["releaseMonth"] = df["releaseDate"].dt.month
df["mainGenre"] = (
    df["genres"]
    .astype(str)
    .str.split("|")
    .str[0]
)

# 4.1 ¿Cuáles son las 10 películas que contaron con más presupuest?
""" top_budget = (
    df.sort_values("budget", ascending=False)
        .loc[:, ["title", "budget"]]
        .head(10)
)
print(top_budget) """

# 4.2 ¿Cuáles son las 10 películas que más ingresos tuvieron?
""" top_revenue = (
    df.sort_values("revenue", ascending=False)
        .loc[:, ["title", "revenue"]]
        .head(10)
)
print(top_revenue) """

# 4.3 ¿Cuál es la película que más votos tuvo?
""" most_votes = df.loc[df["voteCount"].idxmax(), ["title", "voteCount"]]
print(most_votes) """

# 4.4 ¿Cuál es la peor película de acuerdo a los votos de todos los usuarios? 
""" worst_movie = (
    df[df["voteCount"] > 50]
    .sort_values("voteAvg")
    .iloc[0][["title", "voteAvg", "voteCount"]]
)
print(worst_movie) """

# 4.5 ¿Cuántas películas se hicieron en cada año? ¿En qué año se hicieron más películas? Haga un gráfico de barras  
""" movies_per_year = df["releaseYear"].value_counts().sort_index()

plt.figure(figsize=(10,5))
movies_per_year.plot(kind="bar")
plt.title("Cantidad de películas por año")
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.show()

print("Año con más películas:", movies_per_year.idxmax()) """

#4.6 ¿Cuál es el género principal de las 20 películas más recientes? ¿Cuál es el género principal que predomina en el conjunto de datos? Represéntelo usando un gráfico. ¿A qué género principal pertenecen las películas más largas? 
# 20 películas más recientes
""" recent_genres = (
    df.sort_values("releaseDate", ascending=False)
      .head(20)["mainGenre"]
)
print("Las 20 películas más recientes son:\n", recent_genres.value_counts())
 """
# genero predominante
""" genre_counts = df["mainGenre"].value_counts()

plt.figure(figsize=(8,4))
genre_counts.head(10).plot(kind="bar")
plt.title("Género principal predominante")
plt.show() """

# género de las películas más largas.
""" long_movies = (
    df.sort_values("runtime", ascending=False)
        .head(20)["mainGenre"]
)
print("El género de las películas más largas es:\n", long_movies.value_counts())
 """

# 4.7 ¿Las películas de qué genero principal obtuvieron mayores ganancias? 
""" genre_revenue = (
    df.groupby("mainGenre")["revenue"]
      .mean()
      .sort_values(ascending=False)
)

print(genre_revenue.head(10)) """

# 4.8 Cantidad de actores vs ingresos + tendencia temporal
sns.scatterplot(
    data=df,
    x="actorsAmount",
    y="revenue"
)
plt.title("Cantidad de actores vs ingresos")
plt.show()

actors_over_time = (
    df.groupby("releaseYear")["actorsAmount"].mean()
)

actors_over_time.plot()
plt.title("Promedio de actores por año")
plt.show()

