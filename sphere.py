import plotly.graph_objs as go
import numpy as np

# Création des coordonnées pour la sphère
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
r = 1  # Rayon de la sphère
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Créer la figure avec Plotly
sphere = go.Surface(x=x, y=y, z=z)
fig = go.Figure(data=[sphere])

# Mise à jour de la mise en page pour une meilleure visualisation
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
    )
)

# Affichage de la figure
fig.show()
