from kmeans import KMeans
import numpy as np 
import matplotlib.pyplot as plt
from kmeans import *
import timeit

import display
from kmeans import KMeans
import numpy as np 
from kmeans import *
import display
from scipy.optimize import minimize
from scipy.optimize import NonlinearConstraint, LinearConstraint
import time
import numpy as np


def function(name, use_kmeans = True):
    import matplotlib.pyplot as plt

    def f(x, y):
        return x/x

    Hs = 2
    N = 12
    n_clusters = 3
    Is = 40
    Imin = 0.1
    planet_radius = 12

    num_points_per_blob = 20

    # Génération des points pour le premier blob
    mean_phi1, mean_theta1 = np.pi/3, np.pi/4  # Angles moyens du premier blob
    std_dev1 = np.pi/8  # Écart-type pour le premier blob
    phi_blob1 = np.random.normal(mean_phi1, std_dev1, num_points_per_blob)
    theta_blob1 = np.random.normal(mean_theta1, std_dev1, num_points_per_blob)

    # Génération des points pour le deuxième blob
    mean_phi2, mean_theta2 = np.pi/4, 3*np.pi/4  # Angles moyens du deuxième blob
    std_dev2 = np.pi/8  # Écart-type pour le deuxième blob
    phi_blob2 = np.random.normal(mean_phi2, std_dev2, num_points_per_blob)
    theta_blob2 = np.random.normal(mean_theta2, std_dev2, num_points_per_blob)

    # Génération des points pour le troisième blob
    mean_phi3, mean_theta3 = -np.pi/3, 3*np.pi/4  # Angles moyens du troisième blob
    std_dev3 = np.pi/8 # Écart-type pour le troisième blob
    phi_blob3 = np.random.normal(mean_phi3, std_dev3, num_points_per_blob)
    theta_blob3 = np.random.normal(mean_theta3, std_dev3, num_points_per_blob)

    # Fusionner les ensembles de points pour former un seul ensemble de points
    phi = np.concatenate((phi_blob1, phi_blob2, phi_blob3))
    theta = np.concatenate((theta_blob1, theta_blob2, theta_blob3))

    # Assurer que les angles phi restent dans la plage [-pi/2, pi/2]
    phi = np.clip(phi, -np.pi/2, np.pi/2)

    # Fusionner les deux ensembles de points
    P = np.vstack((phi, theta)).T

    population = np.random.randint(10, 101, size=len(P))
    phip = P[:, 0]
    thetap = P[:, 1]

    kmeans = KMeans(n_clusters=n_clusters, max_iters=1000, distance="SPHERICAL")

    kmeans.fit(P)
    y_kmeans = kmeans.predict(P)

    def sigmoid(x, center = 0, M = 100) : 
        return 1/(1+np.exp(-M*(x-center)))

    def distance_sq(r1, r2, phi1, phi2, theta1, theta2) : 
        x1 = r1*np.cos(phi1)*np.cos(theta1)
        y1 = r1*np.cos(phi1)*np.sin(theta1)
        z1 = r1*np.sin(phi1)
        x2 = r2*np.cos(phi2)*np.cos(theta2)
        y2 = r2*np.cos(phi2)*np.sin(theta2)
        z2 = r2*np.sin(phi2)
        return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

    def objectif(x) : 
        somme = 0
        for i in range(N) : 
            dij_sq = distance_sq(planet_radius, planet_radius+Hs, x[2*i], x[2*i], x[2*i+1], x[2*i+1]) 
            somme += Is/(dij_sq)
        return somme

    def contrainte1(x) : 
        somme = 0
        for j in range(len(population)) : 
            sumj = 0
            for i in range(N) : 
                dij_sq = distance_sq(planet_radius, planet_radius+Hs, phip[j], x[2*i], thetap[j], x[2*i+1]) 
                sumj += Is/(dij_sq)
            somme += sigmoid(sumj/population[j], center = Imin, M = 1e2)*population[j]
        return somme/sum(population)


    centers = kmeans.cluster_centers_.reshape(n_clusters*2)
    x0 = np.tile(centers, int(N/n_clusters))
    randomx0 = [np.random.uniform(-5.0, 5.0) for i in range(len(x0))]
    #3 satellite random placer les uns sur les autres
    randomx0same = np.tile([np.random.uniform(-3.0, 15.0) for _ in range(len(centers))], int(N/n_clusters))

    myc1 = NonlinearConstraint(contrainte1, 0.8, 1)
    contraintes = [myc1]

    t0 = time.time()
    if use_kmeans is True :
        print(x0)
        resultat = minimize(objectif, x0, method=name, constraints = contraintes)
    
    if use_kmeans is False:
        resultat = minimize(objectif, randomx0, method=name, constraints = contraintes)
    #print("temps : ", time.time()-t0)
    #print(resultat)
    #print("Résultat de l'optimisation:", resultat.fun)
    #print("Valeurs optimales des variables:", resultat.x)
    #print("Valeur de la contrainte 1 : ", contrainte1(resultat.x))

    def f(phi, theta) : 
        somme = 0
        for i in range(N) : 
            dij_sq = distance_sq(planet_radius, planet_radius+Hs, phi, resultat.x[2*i], theta, resultat.x[2*i+1]) 
            somme += Is/(dij_sq)
        return somme
    """
    mySphere = display.Sphere("Adam", planet_radius, [0, 0, 0], f)

    for i in range(len(P)) : 
        rapport = f(P[i][0], P[i][1])/population[i]
        if rapport > Imin : 
            c = 'lightgreen'
        else : c = 'red'
        mySphere.add_cities(P[i][0], P[i][1], c)
    for i in range(N) : 
        mySphere.add_satellites(resultat.x[2*i], resultat.x[2*i+1], "black", mySphere.radius)
    """
    #mySphere.show()
    return  contrainte1(resultat.x) 


def plot_result():
    resultOptiCOBYLA = []
    resultOptiSLSQP = []
    resultOptiTRUSTCONSTR = []
    resultOptiTNC = []
    for i in range(10):
        resultOptiCOBYLA.append(function('COBYLA'))
        resultOptiSLSQP.append(function('SLSQP'))
        resultOptiTRUSTCONSTR.append(function('trust-constr'))
        resultOptiTNC.append(function('TNC'))
    
    # box plot of result
    plt.figure()
    plt.boxplot([resultOptiCOBYLA, resultOptiSLSQP, resultOptiTRUSTCONSTR, resultOptiTNC])
    plt.xticks([1, 2, 3, 4], ['COBYLA', 'SLSQP', 'trust-constr', 'TNC'])
    plt.xlabel('Solveurs')
    plt.ylabel('Résultat')


def plot_time():
    timeCOBYLA = []
    timeSLSQP = []
    timeTRUSTCONSTR = []
    timeTNC = []
    for i in range(5):
        timeCOBYLA.append(timeit.timeit(lambda: function('COBYLA'), number=1))
        timeSLSQP.append(timeit.timeit(lambda: function('SLSQP'), number=1))
        timeTRUSTCONSTR.append(timeit.timeit(lambda: function('trust-constr'), number=1))
        timeTNC.append(timeit.timeit(lambda: function('TNC'), number=1))
    
    # box plot of time
    plt.figure()
    plt.boxplot([timeCOBYLA, timeSLSQP, timeTRUSTCONSTR, timeTNC])
    plt.xticks([1, 2, 3, 4], ['COBYLA', 'SLSQP', 'trust-constr', 'TNC'])
    plt.xlabel('Solveurs')
    plt.ylabel('Temps (s)')
    plt.show()

def plot_performance_comparison():
    # Liste pour stocker les performances obtenues avec des positions aléatoires
    random_positions_performance = []
    
    # Liste pour stocker les performances obtenues avec K-Means
    kmeans_performance_list = []
    
    # Nombre d'exécutions à comparer
    num_executions = 20
    
    # Exécuter les tests pour obtenir les performances
    for _ in range(num_executions):
        random_performance = function('COBYLA', use_kmeans = False)  # Remplacez 'random' par la fonction que vous utilisez pour les positions aléatoires
        kmeans_performance = function('COBYLA')   # Remplacez 'KMeans' par la fonction que vous utilisez pour K-Means
        
        random_positions_performance.append(random_performance)
        kmeans_performance_list.append(kmeans_performance)
    
    # Créer une liste d'indices pour les exécutions
    execution_indices = [i for i in range(1, num_executions + 1)]
    
    # Tracer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(execution_indices, random_positions_performance, label='Positions Aléatoires')
    plt.plot(execution_indices, kmeans_performance_list, label='K-Means')
    plt.xlabel('Exécution')
    plt.ylabel('Résultat')
    plt.title('Comparaison de performance avec et sans l\'utilisation de K-Means')
    plt.xticks(execution_indices)
    plt.legend()
    plt.grid(True)
    
if __name__ == "__main__":
    #plot_result()
    #plot_time()
    #plt.show()
    plot_performance_comparison()
    plt.show()
    