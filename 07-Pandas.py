import pandas as pd

tabela = pd.read_csv('GasPricesinBrazil_2004-2019.csv', sep=';')
dados = tabela.copy()
del dados['Unnamed: 0']

# Preparação de Dadoss
# print(dados.info())
# analise de valores

dados['DATA INICIAL'] = pd.to_datetime(dados['DATA INICIAL'])
dados['DATA FINAL'] = pd.to_datetime(dados['DATA FINAL'])

conversao = ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO',
             'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']
for atributo in conversao:
    dados[atributo] = pd.to_numeric(dados[atributo], errors='coerce')
# apos mudar o tipo de dados para numéricos houve diferença no numero de registros

# ----- Limpeza de Dados ----
# mask = dados['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()
# para todas as colunas q tiverem valor NaN colocar 0, retorna uma cópia
# dados_pre_fill = dados.fillna(0)
# retornando para o data frame original
# com o parametro value passa um dicionaraio onde infroma a coluna e o valor a ser substituido
# dados = dados_pre_fill

dados.dropna(inplace=True)
dados.to_csv('./Correção dos dados.csv', index=False)
