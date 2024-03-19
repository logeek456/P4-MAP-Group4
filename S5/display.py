import pyvista as pv
import numpy as np


class Sphere() : 

    def __init__(self, name, radius, center, f) : 
        self.name = name
        self.radius = radius
        self.center = center
        self.f = f
        self.dico_couleur = {0: 'r', 1: 'm', 2: 'g', 3: 'y', 4: 'c', 5: 'm', 6: 'k', 7: 'w'}

        n_phi = 1000
        n_theta = 1000
        
        text = pv.read_texture("S5/8k_earth_daymap.jpg")
        
        # Créer un maillage sphérique avec les coordonnées sphériques
        phi = np.linspace(-np.pi/2, np.pi/2, n_phi)
        theta = np.linspace(0, 2*np.pi, n_theta)
        phi, theta = np.meshgrid(phi, theta)
        r = 1  # rayon de la sphère
        x = self.radius * np.cos(phi) * np.cos(theta)
        y = self.radius * np.cos(phi) * np.sin(theta)
        z = self.radius * np.sin(phi)

        # Créer un maillage PolyData avec les coordonnées
        mesh = pv.PolyData(np.c_[x.flatten(order='F'), y.flatten(order='F'), z.flatten(order='F')])

        # Calculer les valeurs de la fonction f sur les points de la sphère
        values = self.f(phi, theta)
        # Ajouter les valeurs en tant que champ de données
        mesh.point_data['Values'] = values.flatten(order='F')
        # Créer un plotter
        self.plotter = pv.Plotter()

        # Ajouter la sphère avec une coloration basée sur les valeurs de f
        self.plotter.add_mesh(mesh, scalars='Values', cmap='jet')

        
        # Ajouter une barre de couleur
        #self.plotter.add_scalar_bar()
        

    def show(self) :

        self.plotter.add_background_image("S5/space.jpg")
        self.plotter.show()
    
    def add_cities(self, phi, theta, c) : 
        x_points = self.radius * np.cos(phi) * np.cos(theta)
        y_points = self.radius * np.cos(phi) * np.sin(theta)
        z_points = self.radius * np.sin(phi)
        self.plotter.add_mesh(pv.Sphere(radius=3*self.radius/100, center=[x_points, y_points, z_points]), color = c)
    
    def add_satellites(self, phi, theta, c, alt) : 
        x_points = (self.radius+alt) * np.cos(phi) * np.cos(theta)
        y_points = (self.radius+alt) * np.cos(phi) * np.sin(theta)
        z_points = (self.radius+alt) * np.sin(phi)
        self.plotter.add_mesh(pv.Sphere(radius=3*self.radius/100, center=[x_points, y_points, z_points]), color = c)






if __name__ == '__main__' : 
    pass

        

    