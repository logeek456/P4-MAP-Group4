from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def spherical_kmeans(X, n_clusters, max_iter=300, tol=1e-4):
    
    X_norm = X / np.linalg.norm(X, axis=1)[:, np.newaxis]

    
    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, tol=tol).fit(X_norm)

    # Obtention des centres initiaux
    centers = kmeans.cluster_centers_

    for _ in range(max_iter):
        # Calculer la distance cosinus entre les points et les centres
        distances = cdist(X_norm, centers, 'cosine')

        # Assigner les points au cluster le plus proche
        labels = np.argmin(distances, axis=1)

        # Mise à jour des centres des clusters
        new_centers = np.array([X_norm[labels == i].mean(axis=0) for i in range(n_clusters)])
        new_centers /= np.linalg.norm(new_centers, axis=1)[:, np.newaxis]

        # Vérifier la convergence
        if np.allclose(centers, new_centers, rtol=tol):
            break

        centers = new_centers
    print(centers, labels)
    return labels, centers

np.random.seed(0)
X = np.random.normal(size=(100, 3))
X /= np.linalg.norm(X, axis=1)[:, np.newaxis]

labels, centers = spherical_kmeans(X, n_clusters=4)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i in range(4):  # n_clusters
    ax.scatter(X[labels == i, 0], X[labels == i, 1], X[labels == i, 2], c=colors[i], label=f'Cluster {i+1}')

ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='black', marker='x', s=100, label='Centers')

u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_surface(x, y, z, color='k', alpha=0.4)


ax.set_axis_off()


ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])


plt.show()