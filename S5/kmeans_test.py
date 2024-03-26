from kmeans import KMeans
import numpy as np 
import matplotlib.pyplot as plt

###################################################################Test 1
print("Test 1")
print("Test effectué en 2D")
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

kmeans = KMeans(n_clusters=3, max_iters=1000, distance="EUCLIDEAN")
    #n_clusters = nombre de clusters avec lequel on travaille
    #init = méthode d'initialisation des centroides, "random" ça veut dire que les centroides sont placés en mode random et "k-means++" c'est une méthode qui donne des centroides optimisés
    #n_init = nombre de fois que l'algorithme va tourner et donner la meilleure solution


kmeans.fit(P)
y_kmeans = kmeans.predict(P)

print("Centroids: ", kmeans.cluster_centers_)
print("Labels: ", y_kmeans)
# Visualiser les clusters
plt.scatter(P[:, 0], P[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, edgecolor='k', c='red')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

print("\n\n")


###################################################################Test 2
print("Test 2")
print("Test effectué en 3D sur une sphère")


num_points_per_blob = 100

# Génération des points pour le premier blob
mean_phi1, mean_theta1 = np.pi/3, np.pi/4  # Angles moyens du premier blob
std_dev1 = np.pi/12  # Écart-type pour le premier blob
phi_blob1 = np.random.normal(mean_phi1, std_dev1, num_points_per_blob)
theta_blob1 = np.random.normal(mean_theta1, std_dev1, num_points_per_blob)

# Génération des points pour le deuxième blob
mean_phi2, mean_theta2 = np.pi/4, 3*np.pi/4  # Angles moyens du deuxième blob
std_dev2 = np.pi/12  # Écart-type pour le deuxième blob
phi_blob2 = np.random.normal(mean_phi2, std_dev2, num_points_per_blob)
theta_blob2 = np.random.normal(mean_theta2, std_dev2, num_points_per_blob)

# Génération des points pour le troisième blob
mean_phi3, mean_theta3 = -np.pi/3, 3*np.pi/4  # Angles moyens du troisième blob
std_dev3 = np.pi/12  # Écart-type pour le troisième blob
phi_blob3 = np.random.normal(mean_phi3, std_dev3, num_points_per_blob)
theta_blob3 = np.random.normal(mean_theta3, std_dev3, num_points_per_blob)

# Fusionner les ensembles de points pour former un seul ensemble de points
phi = np.concatenate((phi_blob1, phi_blob2, phi_blob3))
theta = np.concatenate((theta_blob1, theta_blob2, theta_blob3))

# Assurer que les angles phi restent dans la plage [-pi/2, pi/2]
phi = np.clip(phi, -np.pi/2, np.pi/2)

# Fusionner les deux ensembles de points
P = np.vstack((phi, theta)).T

kmeans = KMeans(n_clusters=3, max_iters=1000, distance="SPHERICAL")

kmeans.fit(P)
y_kmeans = kmeans.predict(P)



dico_couleur = {0: 'r', 1: 'b', 2: 'g', 3: 'y', 4: 'c', 5: 'm', 6: 'k', 7: 'w'};



import pyvista as pv

def _cell_bounds(points, bound_position=0.5):
    """
    Calculate coordinate cell boundaries.

    Parameters
    ----------
    points: numpy.ndarray
        One-dimensional array of uniformly spaced values of shape (M,).

    bound_position: bool, optional
        The desired position of the bounds relative to the position
        of the points.

    Returns
    -------
    bounds: numpy.ndarray
        Array of shape (M+1,)
    """
    if points.ndim != 1:
        raise ValueError("Only 1D points are allowed.")
    diffs = np.diff(points)
    delta = diffs[0] * bound_position
    bounds = np.concatenate([[points[0] - delta], points + delta])
    return bounds

# Fonction à utiliser pour colorier la sphère
def f(x, y):
    return np.cos(2*np.pi*x/360)*np.cos(2*np.pi*y/360)

# Approximate radius of the Earth
RADIUS = 1

# Longitudes and latitudes
x = np.linspace(0, 360, 1000)
y = np.linspace(-90, 90, 1000)
y_polar = 90.0 - y  # grid_from_sph_coords() expects polar angle

xx, yy = np.meshgrid(x, y)

# Évaluation de la fonction f aux coordonnées (x, y)
scalar = f(xx, yy)

# Create arrays of grid cell boundaries, which have shape of (x.shape[0] + 1)
xx_bounds = _cell_bounds(x)
yy_bounds = _cell_bounds(y_polar)
# Vertical levels
# in this case a single level slightly above the surface of a sphere
levels = [RADIUS * 1.01]

grid_scalar = pv.grid_from_sph_coords(xx_bounds, yy_bounds, levels)

# And fill its cell arrays with the scalar data
grid_scalar.cell_data["example"] = np.array(scalar).swapaxes(-2, -1).ravel("C")

Hs = RADIUS

def add_cities(phi, theta, p, c) : 
    x_points = RADIUS * np.cos(phi) * np.cos(theta)
    y_points = RADIUS * np.cos(phi) * np.sin(theta)
    z_points = RADIUS * np.sin(phi)
    p.add_mesh(pv.Sphere(radius=0.02, center=[x_points, y_points, z_points]), color = c)


def add_satellites(phi, theta, p, c) : 
    x_points = (RADIUS+Hs) * np.cos(phi) * np.cos(theta)
    y_points = (RADIUS+Hs) * np.cos(phi) * np.sin(theta)
    z_points = (RADIUS+Hs) * np.sin(phi)
    p.add_mesh(pv.Sphere(radius=0.02, center=[x_points, y_points, z_points]), color = c)



p = pv.Plotter()   
for i in range(len(P)) : 
    phi = P[i][0]
    theta = P[i][1]
    add_cities(phi, theta, p, dico_couleur[y_kmeans[i]])

    
    


# Make a plot

p.add_mesh(pv.Sphere(radius=RADIUS))
p.add_mesh(grid_scalar, clim=[-1, 1], opacity=0.5, cmap="plasma")
p.show()




print("Centroids: ", kmeans.cluster_centers_)
print("Labels: ", y_kmeans)