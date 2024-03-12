import numpy as np
import sys
import matplotlib.pyplot as plt
class KMeans() : 

    def __init__(self, n_clusters, max_iters, distance) :
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.cluster_centers_ = np.zeros((n_clusters, 2))
        self.distance_style = distance
    

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
        distances = self.distance_vect(X, self.cluster_centers_)
        

        # Assign labels based on the nearest centroid
        return np.argmin(distances, axis=1)

    def distance_vect(self, X, centroids) : 
        distances = np.zeros((len(X), len(centroids)))
        for i in range(len(X)) :
            for j in range(len(centroids)) : 
                distances[i][j] = self.distance(X[i], centroids[j])
        return distances
    
    def distance(self, a, b) :  
        if self.distance_style == "EUCLIDEAN" : 
            return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        elif self.distance_style == "SPHERICAL" : 
            phi1 = a[0]; theta1 = a[1]; phi2 = b[0]; theta2 = b[1]
            x1 = np.cos(phi1) * np.cos(theta1)
            y1 = np.cos(phi1) * np.sin(theta1)
            z1 = np.sin(phi1)
            x2 = np.cos(phi2) * np.cos(theta2)
            y2 = np.cos(phi2) * np.sin(theta2)
            z2 = np.sin(phi2)
            dist_sq = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            return np.abs(np.arccos(1 - 0.5 * dist_sq))
        else : 
            raise ValueError("Distance must be either 'EUCLIDEAN' or 'SPHERICAL'")
            

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
        print("intial centroids: ", centroids)
        return centroids



if __name__ == '__main__' : 
    pass
