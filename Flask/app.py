#fichier pour créer une app interactive avec Flask

from flask import Flask, jsonify, request
from flask import redirect, url_for


import folium
import os
import webbrowser
app = Flask(__name__)
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


    satellites_layer = folium.FeatureGroup(name='Satellites')
    coverage_layer = folium.FeatureGroup(name='Zones de couverture')


    # Coordonnées des villes
    

    # Coordonnées des satellites, pareil au pif pour l'exemple
    satellites = {
        "Satellite1": (30, -30),
        "Satellite2": (0, 100),
        "Satellite3": (-40, -60)
    }

    # Rayon de portée des satellites (en km)
    radius = 2000 * 1000

    # Ajouter des marqueurs et des cercles (portées) pour les satellites
    for satellite, (lat, lon) in satellites.items():
        folium.Marker([lat, lon], icon=folium.Icon(color='blue'), popup=satellite).add_to(satellites_layer)
        folium.Circle([lat, lon], radius, color='blue', fill=True, fill_opacity=0.3).add_to(coverage_layer)

    # Ajouter les groupes de couches à la carte
    satellites_layer.add_to(m)
    coverage_layer.add_to(m)

    # Ajouter le contrôle des couches
    folium.LayerControl().add_to(m)

    # Sauvegarder et ouvrir la carte
    return m

# Appeler la fonction
create_map_with_cities_folium()

@app.route('/map')
def mapview():
    # Créer l'objet carte
    m = create_map_with_cities_folium()
    return m._repr_html_()
#fichier pour créer une app interactive avec Flask



@app.route('/')
def home():
    return redirect(url_for('mapview'))

if __name__ == '__main__':
    app.run(debug=True)

