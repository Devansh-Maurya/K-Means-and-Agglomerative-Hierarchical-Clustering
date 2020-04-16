import pandas as pd

df = pd.read_csv('flags_dataset.csv')
colors = {'red': 0, 'green': 1, 'blue': 2, 'gold': 3, 'white': 4, 'black': 5, 'orange': 6}

df.replace(to_replace="red", value=0)

print(df.head())
