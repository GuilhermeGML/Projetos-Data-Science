import pandas as pd

tabela = pd.read_csv('Correção dos dados.csv')
dados = tabela.copy()

# ---- EStátisticas Descritivas -----
# apresenta um data frame com medidas por linhas em cada coluna
descrito = dados.describe()

# print(descrito['PREÇO MÉDIO REVENDA'])
# mostra as estátisticas da coluna espécificada

#print(descrito.loc[['min', 'max', 'mean'], 'PREÇO MÉDIO REVENDA'])
# mostra a coluna e linhas específicados

print(dados['PREÇO MÍNIMO REVENDA'].min())
# valor miniomo
print(dados['PREÇO MÍNIMO REVENDA'].mean())
# valore da média
print(dados['PREÇO MÍNIMO REVENDA'].std())
# desvio padrao

print(dados['ESTADO'].value_counts())
# reotnra em ordem decrescente de linhas para cada estado

