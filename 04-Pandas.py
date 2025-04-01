import pandas as pd

dados = pd.read_csv('GasPricesinBrazil_2004-2019.csv', sep=';')
# carregando um dataset a partir de um arquivo e utilizando um separador

# por padrão o .head() passa as 5 primeiras linhas do Data Frame, caso queira mais
# coloque nos parenteses

# a função .info() monstra as informações da tabela, como valores válidos
# o tipo de dados decada coluna

alunos_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh jedi': [True, True, False]
})
# print(alunos_df.rename(columns={'nome': 'Nome Completo',
#                                 'idade': 'Idade'}))
# utilizado para renomar colunas

# alunos_df_mod = alunos_df.rename(columns={'nome': 'Nome Completo', 'idade': 'Idade'})

# alunos_df.columns = ['Nome', 'Idade', 'Peso', 'Jedi']
# formas de modificar nomes das colunas


#dados['ESTADO'] selecionando uma coluna
# dados.iloc[1] seleciona uma linha q possuie indice 1

num = pd.Series([5, 6, 7], index=['p1', 'p2', 'trab'], name='Notas')

# coluna_copy = dados['PRODUTO'].copy()
# dados['PRODUTO'] = 'Combustível' modifica os valores

# datad['nome da coluna nova] = valores q queira adicionar
# os valores da nova coluna tem que ter o mesmo numero de itens

# index restorna a quantidade de linhas



