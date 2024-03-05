import numpy as np
import numba as nb
from mayavi import mlab
from tvtk.api import tvtk

def auto_sphere(image_file):
    # create a figure window (and scene)
    fig = mlab.figure(size=(600, 600))

    # load and map the texture
    img = tvtk.JPEGReader()
    img.file_name = image_file
    texture = tvtk.Texture(input_connection=img.output_port, interpolate=1)
    # (interpolate for a less raster appearance when zoomed in)

    # use a TexturedSphereSource, a.k.a. getting our hands dirty
    R = 1.5
    Nrad = 180

    # create the sphere source with a given radius and angular resolution
    sphere = tvtk.TexturedSphereSource(radius=R, theta_resolution=Nrad,
                                       phi_resolution=Nrad)

    # assemble rest of the pipeline, assign texture    
    sphere_mapper = tvtk.PolyDataMapper(input_connection=sphere.output_port)
    sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)
    fig.scene.add_actor(sphere_actor)

def plot_cities(population, coords):
    # Create a sphere
    auto_sphere('earth.jpg')

    # Plot the cities
    
    mlab.points3d(coords[:, 0], coords[:,1], coords[:,2], population, scale_factor=0.05)

    # Show the plot
    mlab.show()
    


if __name__ == "__main__":
    """ auto_sphere('earth.jpg')
    coords = []
    for i in range(5):
        coords.append([np.random.uniform(0, np.pi), np.random.uniform(0, 2*np.pi), 1])
    # Spherical coordinates
    theta = np.pi / 4  # angle from the z-axis
    phi = np.pi / 4  # angle from the x-axis in the xy-plane

    # Radius of the sphere
    R = 1

    # Cartesian coordinates
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)

    # Plot the point
    #mlab.points3d(x, y, z, color=(1, 0, 0), scale_factor=0.05)

    # Radius
    R_above = 1.2

    # Cartesian coordinates
    x_above = R_above * np.sin(theta) * np.cos(phi)
    y_above = R_above * np.sin(theta) * np.sin(phi)
    z_above = R_above * np.cos(theta)

    # Plot the point
    #mlab.points3d(x_above, y_above, z_above, color=(0, 1, 0), scale_factor=0.05)"""
    population = np.array([1, 2, 3, 4, 5])
    #Generate coordinates for 5 cities across the sphere
    coords = []
    for i in range(5):
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        coords.append( [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(np.pi/4)])
    coords = np.array(coords)
    polar_coords = np.array([[0, 0, 1], [np.pi/4, 1.5*np.pi/4, 1], [np.pi/2, np.pi/2, 1], [3*np.pi/4, 3*np.pi/4, 1], [np.pi, np.pi, 1]])
    plot_cities(population, coords)

    #mlab.show()



