import numpy as np


def euclidean_distance(city_coords, sat_coords):
    return np.sqrt(np.sum((sat_coords - city_coords)**2))

class Satellite :

    def __init__(self, coordinates, intensity):
        self.coordinates = coordinates
        self.intensity = intensity
    
    def __str__(self):
        return f"Satellite aux coordonées {self.coordinates} avec une intensité de {self.intensity} J"
    
    def get_range(self, cities_coordinates):
        """Retourne la portée du satellite au sol i.e. le rayon du cercle de couverture"""
        return None
    

class City :

    def __init__(self, coordinates, population):
        self.coordinates = coordinates
        self.population = population
    
    def __str__(self):
        return f"Ville aux coordonnées {self.coordinates} avec une population de {self.population}"
    
    def get_demand(self, min_intensity):
        """Retourne la demande totale de la ville"""
        return self.population * min_intensity
    
    def get_intensity(self, satellites):
        """Retourne l'intensité reçue par la ville"""
        intensity = 0
        for satellite in satellites:
            distance = euclidean_distance(self.coordinates, satellite.coordinates)
            intensity += satellite.intensity / distance**2

        return intensity
    
    def satisfied(self, satellites, min_intensity):
        """Retourne si la ville est satisfaite"""
        return int(self.get_intensity(satellites) >= self.get_demand(min_intensity))