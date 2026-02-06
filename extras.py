import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("movies_2026.csv", sep=",", encoding="latin1")

# 5. Genere usted otras seis preguntas que le parezcan interesantes
# porque le permitan realizar otras exploraciones y respóndalas. No puede repetir ninguna
# de las instrucciones anteriores.

#¿Existe relación entre el número de compañías productoras y el desempeño comercial?
# Relación entre número de productoras e ingresos
""" prodco_revenue = (
    df.groupby("productionCoAmount")["revenue"]
        .mean()
        .dropna()
)

plt.figure(figsize=(8,5))
prodco_revenue.plot(marker="o")
plt.title("Ingresos promedio según número de productoras")
plt.xlabel("Número de productoras")
plt.ylabel("Ingresos promedio")
plt.show()

# Correlación
corr_prodco = df[["productionCoAmount", "revenue"]].corr().iloc[0,1]
print("Correlación productionCoAmount vs revenue:", round(corr_prodco, 3))

 """

# Proporción femenina en el elenco
df["femaleRatio"] = df["castWomenAmount"] / (
    df["castWomenAmount"] + df["castMenAmount"]
)

plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="actorsAmount",
    y="femaleRatio"
)
plt.title("Cantidad de actores vs proporción femenina")
plt.xlabel("Cantidad de actores")
plt.ylabel("Proporción de mujeres")
plt.show()

# Correlación
corr_gender = df[["actorsAmount", "femaleRatio"]].corr().iloc[0,1]
print("Correlación actoresAmount vs femaleRatio:", round(corr_gender, 3))
