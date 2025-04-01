import pandas as pd

cal = [2.1, 2.4]
me = [2.5, 5.5]
ga = [7.4, 3.5]
fe = [3.5, 3.5]
notas = list(zip(cal, me, ga, fe))

primeiro = pd.DataFrame(notas, index=['P1', 'P2'], columns=['Cal1', 'M.E', 'GA', 'F.E'])

print(primeiro)
print('-='*20)
segundo = pd.DataFrame(
    {
        "ICC": [7, 9],
        "FIS": [5, 8.5],
        "M.FIN": [7.6, 8.5],
        "GE": [4.5, 5.5],
        "GAE": [3.5, 2.5],
        "CAL2": [2.9, 5.6]
    },
    index=['P1', 'P2']
)

print(segundo)