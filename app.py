from kmeans import kmeans_clustering
from agglomerative_hierarchical import agglomerative_hierarchical_clustering
from util import raise_value_error


if __name__ == '__main__':
    print('Select the algorithm:')
    print('1: K-Means Clustering')
    print('2: Agglomerative Hierarchical Clustering\n')

    choice = int(input('Enter your choice (1/2): '))
    print('\n')

    if choice == 1:
        kmeans_clustering()
    elif choice == 2:
        agglomerative_hierarchical_clustering()
    else:
        raise_value_error('choice')
