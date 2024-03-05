'''
MODELISATION MATHEMATIQUE DE LA SPHERE AVEC PLUSIEURS FONCTIONS 
Fonction de Calcul de Distance, Fonction de Conversion de Coordonnées,
Fonction de Point de Couverture Satellite, Fonction de Calcul de Zone de Couverture
Fonction d'Intersection de Zones de Couverture
'''
import math
import numpy as np


################### distance entre 2 points lat et long###################
def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c
    return distance
#verification dla fonction, ça semble ok! :=)
#dis = distance(49.6833, 5.8167, 50.8466, 4.3528)
#print(dis)



################### CONVERSION DE COORDONNEES LAT LON EN CART ###################
#servira pour la représentation 3D 
def convert(lat, lon):
    lat = math.radians(lat)
    lon = math.radians(lon)
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return x, y, z
#verification dla fonction, ça semble ok! :=)
x, y, z = convert(49.6833, 5.8167)
print(x, y, z)

################### convertion dans l'autre sens ###################
def convert2(x, y, z):
    lat = math.asin(z)
    lon = math.atan2(y, x)
    return math.degrees(lat), math.degrees(lon)
#verification dla fonction, ça semble ok! :=)
#lat, lon = convert2(0.6436807188974397, 0.06557225809075846, 0.7624797774948225)
#print(lat, lon)

