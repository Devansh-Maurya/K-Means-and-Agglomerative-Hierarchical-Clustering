import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from util import raise_value_error


def kmeans_clustering():
    init_methods = ['k-means++', 'random']

    print('Select the centroid initialization Method:')
    print('1: ', init_methods[0])
    print('2: ', init_methods[1])
    print('3: Compare both the above methods')

    init = int(input('Enter your choice (1/2/3): '))

    if init in (1, 2):
        init_method = [init_methods[init - 1]]
    elif init == 3:
        init_method = init_methods
    else:
        raise_value_error('Centroid Initialization method')

    print('\nHow do you want to run the algorithm: ')
    print('1: Enter a value of k manually')
    print('2: Run for all the values of k from 1 to 10')

    mode = int(input('Enter your choice (1/2): '))

    if mode == 1:
        k = int(input('\nEnter the value of k: '))
        run_algorithm(init_method, k)
    elif mode == 2:
        run_algorithm(init_method)


def run_algorithm(init_methods, k=0):

    def run_algorithm_for_k(k, init_method):
        kmeans = KMeans(n_clusters=k, init=init_method)
        kmeans.fit(x)
        errors.append(kmeans.inertia_)

    df = pd.read_csv('dataset/graduate-admissions/graduate_admissions_dataset.csv')

    # Select all attributes except:
    # Serial No.: Not relevant as its unique for every record
    # Research: Not being considered as it is a class attribute with classes as 0 and 1
    attrs = [i for i in range(1, 7)]

    # Select all records. First row is excluded as its the column titles
    x = df.iloc[1:, attrs].values
    # Apply pre-processing to scale all the values to have approx. same mean and S.D.
    x = preprocessing.scale(x)

    for i, init_method in enumerate(init_methods):
        errors = []
        print('\nSSE error for k (' + init_method + '):')
        if k == 0:
            for i in range(1, 11):
                run_algorithm_for_k(i, init_method)
                print(str(i) + '\t:\t', errors[i-1])
            plt.plot(range(1, 11), errors, label=init_method)
            plt.title('Comparison among various k values')
            plt.xlabel('No. of clusters')
            plt.ylabel('Error')
            plt.legend()
            plt.show()
        else:
            run_algorithm_for_k(k, init_method)
            print(str(k) + '\t:\t', errors[0])


if __name__ == '__main__':
    kmeans_clustering()
