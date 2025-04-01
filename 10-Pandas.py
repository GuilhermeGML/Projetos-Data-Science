import pandas as pd

tabela = pd.read_csv('Correção dos dados.csv')
dados = tabela.copy()

# ----- AGRUPAMENTO -----
grupos = dados.groupby(['REGIÃO'])
# print(grupos.indices)
# mostra os indices que cada grupo possue

# print(grupos.get_group('CENTRO OESTE'))
# mostra um data frame da região especificada

# print(grupos.describe())
# mostra algumas estátisticas descritivas das regiões

# agurpando com mais de uma especificação
#grupos = dados.groupby(['REGIÃO', 'PRODUTO'])
# print(grupos.group)
# print(grupos['PREÇO MÉDIO REVENDA'].mean())

print(grupos['PREÇO MÉDIO REVENDA'].agg([min, max]))