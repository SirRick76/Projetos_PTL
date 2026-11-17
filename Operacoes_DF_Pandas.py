import pandas as pd
import matplotlib.pyplot as plt

dc=pd.read_csv("california_housing_test.csv")
df=pd.DataFrame(dc)
#print (df)

#Etapa 1-Exploração e conhecimento do conjunto de dados
'''
print("Dimensão do conjunto de dados",df.shape)
print(df.head(5))
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.isna())
print(df.isna().sum())
'''

#Etapa 2- Seleção, consulta e filtragem de dados
'''
print(df["longitude"])
print(df[["longitude","latitude","median_house_value"]])
print(df.loc[0,["longitude","latitude","median_house_value"]])
print(df[df["median_income"]>5])
print(df[df["median_house_value"]<150000])
print(df[df["housing_median_age"]== 20])
print(df[df["population"]>1000])
#Que zonas apresentam rendimento superior a 5 e valor mediano das habitações superior a 300 000 dólares
print(df[(df["median_income"]> 5) & (df["median_house_value"])]> 300000)
#Que zonas apresentam um rendimento mediano entre 3 e 5?
print(df[df["median_income"].between(3,5)])
'''

#Etapa 3 – Análise e caracterização dos dados
print("Valor mínimo:", df["median_house_value"].min())
print("Valor máximo:", df["median_house_value"].max())
print("Valor médio:", df["median_house_value"].mean())
print("Mediana:", df["median_house_value"].median())
print("Número de registos", df["median_house_value"].count())

print(df["median_house_value"].describe())
#Distribuição dos valores medianos das habitações
df["median_house_value"].hist()
plt.title("Distribuição dos valores das habitações")
plt.xlabel("Valor mediano (€)")
plt.ylabel("Número de registos")
plt.show()

#Relação entre rendimento mediano e valor das habitaçõoe
plt.scatter(df["median_income"], df["median_house_value"])

plt.title("Rendimento mediano vs valor das habitações")
plt.xlabel("Rendimento mediano")
plt.ylabel("Valor mediano das habitações (€)")
plt.show()

#Distribuição geográfica dos registos
plt.scatter(
    df["longitude"],
    df["latitude"],
    c=df["median_house_value"],
    cmap="viridis"
)

plt.title("Distribuição geográfica dos valores das habitações")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label="Valor mediano das habitações (€)")
plt.show()

#Distribuiçao dos valores medianos das habitações
plt.boxplot(df["median_house_value"])
plt.title("Distribuição dos valores das habitações")
plt.ylabel("Valor mediano(€)")
plt.show()