import pandas as pd

dados = [4.5, 5.3, 9.4, 5.2, 6.1, 7.3]
dados2 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
dados3 = [-1.7, 2.5, -6.0, 7.5, -35.0, 56.0]
dados_tot = list(zip(dados, dados2, dados3))
datas = pd.date_range("20221226", periods=6)
df = pd.DataFrame(dados_tot, index=datas, columns=['P1', 'P2', 'P3'])

print(df)
