from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def spherical_kmeans(X, n_clusters, max_iter=300, tol=1e-4):
    # Normaliser les données à la surface de la sphère (rayon 1)
    X_norm = X / np.linalg.norm(X, axis=1)[:, np.newaxis]

    # Initialisation avec KMeans classique
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

    return labels, centers

# Exemple d'utilisation
np.random.seed(0)
X = np.random.normal(size=(100, 3))
X /= np.linalg.norm(X, axis=1)[:, np.newaxis]

# Application du K-means sphérique
labels, centers = spherical_kmeans(X, n_clusters=6)

# Création de la figure 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Couleurs pour les différents clusters
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# Tracer les points
for i in range(6):#n_clusters
    ax.scatter(X[labels == i, 0], X[labels == i, 1], X[labels == i, 2], c=colors[i], label=f'Cluster {i+1}')

# Tracer les centres des clusters
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='black', marker='x', s=100, label='Centers')

# Tracer la sphère
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="k", alpha=0.1)

# Configuration des axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.legend()

# Affichage du graphique
plt.show()