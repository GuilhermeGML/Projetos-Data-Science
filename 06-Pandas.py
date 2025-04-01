import pandas as pd

tabela = pd.read_csv('GasPricesinBrazil_2004-2019.csv', sep=';')
dados = tabela.copy()

# -----Filtrando amostras ------
del dados['Unnamed: 0']
# print(dados['ESTADO'].unique())  retorna valores unicos sem repetição

# salvando a series em uma várial
selecao = dados['ESTADO'] == 'SAO PAULO'
# print(dados[selecao]) ou print(dados.loc[selecao])
selecao_sp = dados[selecao]
# print(dados.query('ESTADO == "SAO PAULO"'))
# boa pratica é salvar a filtragem em uma outra variavel

# selecao_sp.reset_index()  reseta os index para 0 ate n-1
# drop = true elimina os indeces anteriores
# implace = true altera no proprio data frame
# var = dados.query('ESTADO == "SAO PAULO"'.reset_index(drop=true) tudo em uma linha

#rj_p2 = (dados['ESTADO'] == 'RIO DE JANEIRO') & (dados['PREÇO MÉDIO REVENDA'] > 2)
# filtragem de dados com mais de uma espeficicação

# filtragem = dados['ESTADO'] == 'RIO DE JANEIRO'
# postos_rj = dados[filtragem]
# filtragem_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2
# resultado = postos_rj[filtragem_2]
# print(resultado)
# filtragem mais longa, porem se o data frame for muito grnade é melhor

# filtragem por estado
# filtragem1 = (dados['ESTADO'] == 'RIO DE JANEIRO') | (dados['ESTADO'] == 'SAO PAULO')
# postos_sp_rj = dados[filtragem1]
# filtragem produto e preço
# filtragem2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM') & (postos_sp_rj['PREÇO MÉDIO REVENDA'] > 2)
# resultado = postos_sp_rj[filtragem2]
# print(resultado)

# iterando
# utilizando um for para data frame
# indicado apenas para pequenos conjuntos, pois é lento
#for index, row in dados.head(10).iterrows():
#print(f'indice{index} ==> {row["ESTADO"]}')



