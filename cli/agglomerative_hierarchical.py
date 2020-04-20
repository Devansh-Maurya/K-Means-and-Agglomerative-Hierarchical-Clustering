import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn import preprocessing
import scipy.cluster.hierarchy as shc
import numpy as np
import matplotlib.pyplot as plt
from util import raise_value_error


def agglomerative_hierarchical_clustering():
    pass


def run_algorithm():
    df = pd.read_csv('dataset/graduate-admissions/Admission_Predict.csv')

    # Select all attributes except:
    # Serial No.: Not relevant as its unique for every record
    # Research: Not being considered as it is a class attribute with classes as 0 and 1
    attrs = [i for i in range(1, 7)]

    # Select all records. First row is excluded as its the column titles
    x = df.iloc[1:, attrs].values
    # Apply pre-processing to scale all the values to have approx. same mean and S.D.
    x = preprocessing.scale(x)

    cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
    cluster.fit_predict(x)
    print(cluster.labels_)
    plt.title('Dendogram')
    dend = shc.dendrogram(shc.linkage(x, method='ward'))
    plt.show()



if __name__ == '__main__':
    #agglomerative_hierarchical_clustering()
    run_algorithm()
