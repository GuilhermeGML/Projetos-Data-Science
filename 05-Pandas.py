import pandas as pd

tabela = pd.read_csv('GasPricesinBrazil_2004-2019.csv', sep=';')
dados = tabela.head().copy()


# print(dados.iloc[1])  selecionado a linha 1 por meio do indice do dataframe

# print(dados.iloc[:5]) selecionando várias linhas

# para colunas print(dados.iloc[1, 4]) linha 1 coluna 4

# .loc seleciona elementos pelos seus rotulo print(dados.loc[nome do indice])

# print(dados['ESTADO']) print(dados['DATA INICIAL'])
# print(dados.ESTADO) print(dados.DATA INICIAL )
# print(dados.loc[:, 'ESTADO'])
# lista para mais colunas ou linhas


# ---- adicionando colunas ------
# dados['Game'] = 'DEFAULT'
# dados['Game2'] = range(dados.shape[0])

# ----- removendo colunas -----
# del dados['Unnamed: 0']
# del dados['Game']
# del dados['Game2']

# print(dados)

dados.to_csv('Dados_Modificados', index=False, sep=',')
