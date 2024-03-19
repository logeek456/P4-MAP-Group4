import numpy as np
import numpy as np
import pyvista as pv

# Définir une fonction arbitraire f sur une sphère avec les coordonnées sphériques phi et theta
def custom_function(phi, theta):
    # Exemple : fonction dépendant de phi et theta
    return np.sin(phi) * np.cos(theta)

# Nombre de points de discrétisation pour phi et theta
n_phi = 1000
n_theta = 1000

# Créer un maillage sphérique avec les coordonnées sphériques
phi = np.linspace(-np.pi/2, np.pi/2, n_phi)
theta = np.linspace(0, 2*np.pi, n_theta)
phi, theta = np.meshgrid(phi, theta)
r = 1  # rayon de la sphère
x = r * np.cos(phi) * np.cos(theta)
y = r * np.cos(phi) * np.sin(theta)
z = r * np.sin(phi)

# Créer un maillage PolyData avec les coordonnées
mesh = pv.PolyData(np.c_[x.flatten(order='F'), y.flatten(order='F'), z.flatten(order='F')])

# Calculer les valeurs de la fonction f sur les points de la sphère
values = custom_function(phi, theta)

# Ajouter les valeurs en tant que champ de données
mesh.point_data['Values'] = values.flatten(order='F')

# Créer un plotter
plotter = pv.Plotter()

# Ajouter la sphère avec une coloration basée sur les valeurs de f
plotter.add_mesh(mesh, scalars='Values', cmap='jet')

# Ajouter une barre de couleur
plotter.add_scalar_bar()

# Afficher la visualisation
plotter.show()

