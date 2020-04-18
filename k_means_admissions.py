import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/graduate-admissions/Admission_Predict.csv')

attrs = [i for i in range(1, 7)]
attrs = [1,6]

x = df.iloc[1:, attrs].values
x = preprocessing.scale(x)

clusters = 4

pca = PCA(n_components=2).fit_transform(x)

print(pca)

kmeans = KMeans(n_clusters=clusters)
y_kmeans5 = kmeans.fit_predict(x)

result = [0 for i in range(clusters)]
property = {}

for i, y in enumerate(y_kmeans5):
    country = df.iloc[i, 0]
    #    print(country, y)
    if y not in property:
        property[y] = []
    property[y].append(country)
    result[y] += 1

for k, v in property.items():
    print(k, ': ', v)


#plt.scatter(x[:, 0], x[:, 1], c=y_kmeans5, cmap='rainbow')
# plt.bar(range(len(result)), result)
plt.scatter(df.loc[1:, 'GRE Score'], df.loc[1:, 'TOEFL Score'], c=kmeans.labels_.astype(float))
centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=169, color='b')
plt.show()

#Elbow method
# Error =[]
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i).fit(x)
#     kmeans.fit(x)
#     Error.append(kmeans.inertia_)
# plt.plot(range(1, 11), Error)
# plt.title('Elbow method')
# plt.xlabel('No of clusters')
# plt.ylabel('Error')
# plt.show()
