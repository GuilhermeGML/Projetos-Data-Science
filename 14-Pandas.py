import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Agua': [200, 200, 200],
                   'Fogo': [300, 300, 300],
                   'Terra': [400, 400, 400],
                   'Ar': [500, 500, 500],
                   'Luz': [700, 700, 700],
                   'Escuridão': [700, 700, 700]})

df.plot(kind='bar')
# tipo do grafico
plt.ylabel('Poder')
# denominação do eixo Y
plt.xlabel('Parametros')
# denominação do eixo X
plt.xticks([0, 1, 2], ['Froça', 'Defesa', 'Vida'])
# altera os nomes dos valores de X
plt.title('Genius')
# titulo do gráfico
plt.show()
