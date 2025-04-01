import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [10, 20, 30, 40],
                   'C': [100, 200, 300, 400]},
                  index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])


# eixo = 0 navega pelas colunas
# eixo = 1 navega pelas linhas

df.loc['Linha 5'] = df.apply(lambda series: series.sum(), axis=0)
df['SOMA'] = df[['A', 'B', 'C']].apply(lambda series: series.sum(), axis=1)
df['MÉDIA'] = df[['A', 'B', 'C']].apply(lambda series: series.mean(), axis=1)

df['C*2'] = df['C'].apply(lambda x: x * 2)



print(df)




