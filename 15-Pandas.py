import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('Correção dos dados.csv')
dados = tabela.copy()

reg = dados.groupby('REGIÃO')
# organiza por região
reg_sul = reg.get_group('SUL')
# região especifica a Sul
graf1 = reg_sul['MARGEM MÉDIA REVENDA']
# unico dado do data frame analisado é Margem de revenda
graf1.plot(kind='bar')
plt.ylabel('Valores')
plt.xlabel('Preço')
plt.title('MARGEM MÉDIA REVENDA DA REGIÃO SUL')
plt.show()



