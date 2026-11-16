import pandas as pd

salarios=pd.Series([1200,1500,1350,1800])
print(salarios)

vendas = pd.Series(
    [1500,2300,1800],
    index=["Janeiro","Fevereiro","Março"]
)
print(vendas)
print(vendas.index)
print(vendas.values)
print(vendas.dtype)
print(vendas.shape)
print(vendas.ndim)
print(vendas.size)
print(vendas.name)
print(vendas.empty)

dados = {
    "Produto":["Computador","Monitor","Teclado","Rato"],
    "Quantidade":[5,8,12,15],
    "Preço":[7500.00,180.00,35.00,20.00]
}

df=pd.DataFrame(dados)
print(df)

dc=pd.read_csv("california_housing_test.csv")
print(dc)
dj=pd.read_json("funcionarios.json")
print(dj)
dh=pd.read_json("habitacoes.json")
dh=pd.json_normalize(dh.to_dict(orient="records"))
print(dh)
de = pd.read_excel("vendas.xlsx")
print(de)

dfev= pd.read_excel("vendas.xlsx",sheet_name="Fevereiro")

print(dfev)

dados=pd.read_excel("vendas.xlsx",sheet_name=None)
print(dados)
print(dados.keys())

df_janeiro= dados["Janeiro"]
print(df_janeiro)