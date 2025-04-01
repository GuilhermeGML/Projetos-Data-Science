import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

datas = pd.date_range("20130101", periods=6)
# print(datas)

df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list("ABCD"))
# print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
# print(df2)

# print(df.head()) Exibe todo o Data Frame

# print(df.tail(3)) Exibe apenas a parte pedida no tail por linhas

# print(df.index) é mostrado o denominador de cada linha

# print(df.columns) é mostrado o denominador de cada coluna

# print(df.to_numpy()) print(df2.to_numpy()) mostra os dados q estão no DataFrame

# print(df.describe()) mostra um resumo estatístico rápido de seus dados

# print(df.t()) trasnpom os dados, ou seja, inverte as linhas pelas colunas

# print(df.sort_index(axis=1, ascending=False)) calssifica por eixo

# print(df[0:3]) seleciona apenas uma parte do Data Frame

# print(df.loc[dates()] para obter uma seção transversal usando uma etiqueta

# print(df[df['A'] > 0]) selecionando dados

df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# A forma acima adiciona uma coluna na tabela
# print(df3)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df['F'] = s1

# print(df)
# DataFrame.dropna()remove todas as linhas com dados ausentes
# DataFrame.fillna()preenche dados ausentes

