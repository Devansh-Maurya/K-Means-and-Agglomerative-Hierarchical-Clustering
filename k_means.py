import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/flags_dataset.csv')
print(df.head())

attrs = [i for i in range(7, 28)]
attrs.remove(17)

x = df.iloc[:, attrs].values

kmeans5 = KMeans(n_clusters=7)
y_kmeans5 = kmeans5.fit_predict(x)

result = [0 for i in range(8)]
counts = []

for i, y in enumerate(y_kmeans5):
    print(df.iloc[i, 0], y)
    result[y] += 1

#plt.scatter(x[:, 0], x[:, 1], c=y_kmeans5, cmap='rainbow')
plt.bar(range(len(result)), result)
plt.show()

