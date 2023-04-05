import os
import requests
import altair as alt
import pandas as pd


lista_suja = 'https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/cadastro_de_empregadores-atualizacao-extraord-09-mar-2023.xlsx' 
df = pd.read_excel(lista_suja, skiprows=5)
df

#excluir colunas vazias
df.drop(df.iloc[:, 10:96], inplace=True, axis=1)
df

#excluir linhas as quais não contém dados
df2=df.dropna()
df2

Soma_Trabalhadores = df2['Trabalhadores envolvidos'].sum()
print(Soma_Trabalhadores)

Trabalhadores_UF = df2.groupby('UF')['Trabalhadores envolvidos'].sum().sort_values(ascending=False)
Trabalhadores_UF

Trabalhadores_UF = Trabalhadores_UF.reset_index()
Trabalhadores_UF

a = df2['CNAE'].value_counts()
print(a)

a=a.reset_index()

a.info()

repeticoesCNAE = df2.pivot_table(index = ['CNAE'], aggfunc ='size')


Ranking_CNAE = repeticoesCNAE.sort_values(ascending=False)

Ranking_CNAE = Ranking_CNAE.reset_index()
Ranking_CNAE

Ranking_CNAE['CNAE'] = Ranking_CNAE['CNAE'].astype(str)

CNAES = {'0134-2/00': 'Cultivo de Café','0151-2/01': 'Criação de bovinos', '0210-1/08' : 'Produção de Carvão Vegetal', '9700-5/00' : 'Trabalho doméstico' }

b = Ranking_CNAE.replace(CNAES)

Return "Ok"
