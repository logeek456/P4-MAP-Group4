import numpy as np
import sys


from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


class KMeans() : 

    def __init__(self, n_clusters, max_iters) :
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.cluster_centers_ = np.zeros((n_clusters, 2))
    
    

    def fit(self, X):
        # Initialize centroids randomly
        self.cluster_centers_ = self.initialize(X, self.n_clusters)
        
        for _ in range(self.max_iters):
            # Assign each data point to the nearest centroid
            labels = self.predict(X)
            
            # Update centroids
            new_centroids = self._update_centroids(X, labels)
            
            # Check for convergence
            if np.all(self.cluster_centers_ == new_centroids):
                break
                
            self.cluster_centers_ = new_centroids

        
    
    def _update_centroids(self, X, labels):
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])
        return new_centroids

    def predict(self, X) : 
         # Compute distances from each data point to centroids
        distances = np.linalg.norm(X[:, np.newaxis] - self.cluster_centers_, axis=2)

        print("Ceci est ma distance : ", distances)
        print("ceci est mon X : ", X[:, np.newaxis])
        print("ceci est mon cluster center : ", self.cluster_centers_)
        # Assign labels based on the nearest centroid
        return np.argmin(distances, axis=1)

    def distance_vect(self, X, centroids) : 
        distances = np.zeros((len(X), len(centroids)))
        for i in range(len(X)) :
            for j in range(len(centroids)) : 
                distances[i][j] = self.distance(X[i], centroids[j])
        return distances
    
    def distance(self, a, b) :  
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def initialize(self, data, k):
        '''
        initialized the centroids for K-means++
        inputs:
            data - numpy array of data points having shape (200, 2)
            k - number of clusters 
        '''
        ## initialize the centroids list and add
        ## a randomly selected data point to the list
        centroids = []
        centroids.append(data[np.random.randint(
                data.shape[0]), :])
        
    
        ## compute remaining k - 1 centroids
        for c_id in range(k - 1):
            
            ## initialize a list to store distances of data
            ## points from nearest centroid
            dist = []
            for i in range(data.shape[0]):
                point = data[i, :]
                d = sys.maxsize
                
                ## compute distance of 'point' from each of the previously
                ## selected centroid and store the minimum distance
                for j in range(len(centroids)):
                    temp_dist = self.distance(point, centroids[j])
                    d = min(d, temp_dist)
                dist.append(d)
                
            ## select data point with maximum distance as our next centroid
            dist = np.array(dist)
            next_centroid = data[np.argmax(dist), :]
            centroids.append(next_centroid)
            dist = []
            
        return centroids



# Generate synthetic data using sklearn.datasets.make_blobs
points_per_cluster = 20
points = []
centers = np.array([[0, 0], [10, 0], [5, 10]])
for center in centers:
    # Générer des points aléatoires autour du centre du cluster
    cluster_points = np.random.normal(loc=center, scale=3, size=(points_per_cluster, 2))
    points.extend(cluster_points)

points = np.array(points)
xp = points[:, 0]
yp = points[:, 1]


P = np.vstack((xp, yp)).T

kmeans = KMeans(n_clusters=3, max_iters=1000)
    #n_clusters = nombre de clusters avec lequel on travaille
    #init = méthode d'initialisation des centroides, "random" ça veut dire que les centroides sont placés en mode random et "k-means++" c'est une méthode qui donne des centroides optimisés
    #n_init = nombre de fois que l'algorithme va tourner et donner la meilleure solution


kmeans.fit(P)
y_kmeans = kmeans.predict(P)


# Visualiser les clusters
plt.scatter(P[:, 0], P[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, edgecolor='k', c='red')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
