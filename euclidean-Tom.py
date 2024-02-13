import numpy as np 
import matplotlib.pyplot as plt # Pour les graphiques
from matplotlib.patches import Circle # les cercles de portées des sate
import vtk # Pour la visualisation 3D, + tard
import cartopy.crs as ccrs # Pour les cartes géographiques
import cartopy.feature as cfeature # Pour ajouter les continents et les terres
import folium # pour créer une carte interactive
import webbrowser # ouvrir le fichier HTML dans le navigateur par défaut
import os # ouvrir ds le navigateur

# Créer une carte avec les villes et les satellites à METTRE À LA FIN Et on 
# remplace les villes et sate par les réponses du solveur

def create_map_with_cities_folium():
    # Centre de la carte pour l'affichage initial
    m = folium.Map(location=[20, 0], zoom_start=2, 
                   min_lat=-90, max_lat=90, min_lon=-180, max_lon=180, max_bounds=True)

    # Ajout d'un panneau d'information
    info_html = '''
        <div style="padding: 6px; background-color: white; width: 200px;">
            <h4>Information Satellite</h4>
            <p>Cliquez sur un satellite pour voir les infos.</p>
        </div>
    '''
    iframe = folium.IFrame(html=info_html, width=250, height=100)
    folium.Marker([20, 0], icon=folium.Icon(icon='info-sign'), popup=folium.Popup(iframe)).add_to(m)
    covered_population = 8000
    total_population = 10000
    coverage_percentage = (covered_population / total_population) * 100

    # Ajouter un élément HTML pour le pourcentage
    coverage_html = f'''
        <div style="position: fixed; top: -350px; right: -600px; background-color: white; padding: 6px;">
            <h4>Couverture Satellitaire</h4>
            <p>{coverage_percentage:.2f}% de couverture</p>
        </div>
    '''
    iframe = folium.IFrame(html=coverage_html, width=200, height=100)
    folium.map.Marker(
        [0, 0], 
        icon=folium.DivIcon(
            html=coverage_html
        )
    ).add_to(m)


    # couches
    cities_layer = folium.FeatureGroup(name='Villes')
    satellites_layer = folium.FeatureGroup(name='Satellites')
    coverage_layer = folium.FeatureGroup(name='Zones de couverture')


    # Coordonnées des villes, j'en ai générées au pif pour l'exemple
    cities = {
        "Tokyo": (35.6895, 139.6917),
        "Delhi": (28.7041, 77.1025),
        "Shanghai": (31.2304, 121.4737),
        "Sao Paulo": (-23.5505, -46.6333),
        "Mumbai": (19.0760, 72.8777)
    }

    # Coordonnées des satellites, pareil au pif pour l'exemple
    satellites = {
        "Satellite1": (30, -30),
        "Satellite2": (0, 100),
        "Satellite3": (-40, -60)
    }

    # Rayon de portée des satellites (en km)
    radius = 2000 * 1000

    # Ajouter des marqueurs pour les villes
    for city, (lat, lon) in cities.items():
        folium.Marker([lat, lon], popup=city).add_to(cities_layer)

    # Ajouter des marqueurs et des cercles (portées) pour les satellites
    for satellite, (lat, lon) in satellites.items():
        folium.Marker([lat, lon], icon=folium.Icon(color='blue'), popup=satellite).add_to(satellites_layer)
        folium.Circle([lat, lon], radius, color='blue', fill=True, fill_opacity=0.3).add_to(coverage_layer)

    # Ajouter les groupes de couches à la carte
    cities_layer.add_to(m)
    satellites_layer.add_to(m)
    coverage_layer.add_to(m)

    # Ajouter le contrôle des couches
    folium.LayerControl().add_to(m)

    # Sauvegarder et ouvrir la carte
    map_file = 'map.html'
    m.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))

# Appeler la fonction
create_map_with_cities_folium()


# Créer une fenêtre où on fait genre que les satellites et les villes ont été trouvées
def create_map_with_cities():
    # Coordonnées des villes : [latitude, longitude]
    cities = {
        "Tokyo": (35.6895, 139.6917),
        "Delhi": (28.7041, 77.1025),
        "Shanghai": (31.2304, 121.4737),
        "Sao Paulo": (-23.5505, -46.6333),
        "Mumbai": (19.0760, 72.8777)
    }
    # Coordonnées des satellites : [latitude, longitude]
    satellites = {
        "Satellite1": (30, -30),
        "Satellite2": (0, 100),
        "Satellite3": (-40, -60)
    }
    # Rayon de portée des satellites (en degrés)
    radius = 20
    # Créer une figure matplotlib
    plt.figure(figsize=(10, 5))

    # Définir la projection rectangulaire
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Ajouter les continents et les côtes
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.COASTLINE)

    # Ajouter les villes
    for city, (lat, lon) in cities.items():
        plt.plot(lon, lat, 'ro', transform=ccrs.Geodetic())
        plt.text(lon, lat, city, transform=ccrs.Geodetic())
    # Ajouter les satellites et leur portée
    for satellite, (lat, lon) in satellites.items():
        plt.plot(lon, lat, 'bo', transform=ccrs.Geodetic())  # Marqueur bleu pour le satellite
        circle = Circle((lon, lat), radius, color='blue', alpha=0.3, transform=ccrs.Geodetic())
        ax.add_patch(circle)

    # Limiter l'étendue de la carte
    ax.set_extent([-180, 180, -60, 60], crs=ccrs.PlateCarree())

    # Afficher la carte
    plt.show()

# Appeler la fonction
create_map_with_cities()



"""
CODE POUR MINIMISER LA DISTANCE ENTRE LES SATELLITES ET LES VILLES SUR UN RECTANGLE

"""


def euclidean_distance(p1, p2):# Fonction pour calculer la distance euclidienne entre deux points
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Fonction pour calculer la distance totale entre sate LE PLUS PROCHE et villes
#def total_distance(satellite_positions, cities_coordinates, cities_weights):
#    total_dist = 0
#    for i, city_coord in enumerate(cities_coordinates):
#        min_dist = np.inf
#        for satellite_pos in satellite_positions:
#            distances = [euclidean_distance(city_coord, satellite_position) for satellite_position in satellite_positions]
#            dist = min(distances)
#            if dist < min_dist:
#                min_dist = dist
#        total_dist += min_dist * cities_weights[i]
#    return total_dist

# Fonction pour vérifier si l'intensité reçue est acceptable, on dit que intensité est une distance et on met un treshold
def is_intensity_acceptable(satellite_positions, city_coordinates, intensity_threshold):
    acceptable_intensity = np.zeros(len(city_coordinates), dtype=int)
    for i, city_coord in enumerate(city_coordinates):
        distances = [euclidean_distance(city_coord, satellite_position) for satellite_position in satellite_positions]
        min_dist = min(distances)
        if min_dist <= intensity_threshold:
            acceptable_intensity[i] = 1
    return acceptable_intensity

# Fonction pour calculer si au moins 80% de la population a accès à une couverture d'intensité acceptable
def is_coverage_acceptable(satellite_positions, city_coordinates, cities_weights, intensity_threshold):
    acceptable_intensity = is_intensity_acceptable(satellite_positions, city_coordinates, intensity_threshold)
    total_population = np.sum(cities_weights)
    covered_population = np.sum(cities_weights * acceptable_intensity)
    coverage_percentage = (covered_population / total_population) * 100
    return coverage_percentage >= 80

#fonction objectif pour minimiser la distance totale entre les satellites et les villes



#créé une sphère qui représente la terre de rayon r
def create_earth(r):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z
#fonction qui calcule le pourcentage de couverture pour une intensité donnée sur une sphere d'un rayon donné
def coverage_percentage_on_sphere(satellite_positions, city_coordinates, cities_weights, intensity_threshold, r):
    acceptable_intensity = is_intensity_acceptable(satellite_positions, city_coordinates, intensity_threshold)
    total_population = np.sum(cities_weights)
    covered_population = np.sum(cities_weights * acceptable_intensity)
    coverage_percentage = (covered_population / total_population) * 100
    return coverage_percentage

#solveur pour minimiser la distance totale entre les satellites et les villes 
