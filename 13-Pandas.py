import pandas as pd

tabela = pd.read_csv('Correção dos dados.csv')
dados = tabela.copy()

# print(dados.info())

ano_2019 = dados['ANO'] != 2019
sem_2019 = dados[ano_2019].reset_index(drop=True)
# ------------------------------------------------------

grupos = dados.groupby('REGIÃO')['PRODUTO'].value_counts()

# --------------------------------------------------------------
geral = dados.query('PRODUTO == "GASOLINA COMUM" and ESTADO == "SÂO PAULO" and ANO == 2018')

# -------------------------------------







