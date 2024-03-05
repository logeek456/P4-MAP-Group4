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
    R = 1
    Nrad = 180

    # create the sphere source with a given radius and angular resolution
    sphere = tvtk.TexturedSphereSource(radius=R, theta_resolution=Nrad,
                                       phi_resolution=Nrad)

    # assemble rest of the pipeline, assign texture    
    sphere_mapper = tvtk.PolyDataMapper(input_connection=sphere.output_port)
    sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)
    fig.scene.add_actor(sphere_actor)


auto_sphere('earth.jpg')
mlab.show()



# Generate a sphere representing the Earth
r = 6371  # Earth's radius in kilometers
theta, phi = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = r*np.sin(phi)*np.cos(theta)
y = r*np.sin(phi)*np.sin(theta)
z = r*np.cos(phi)

# Load topography data (you can use your own data)
topo = np.loadtxt('topography_data.txt')

# Plot Earth's surface
surface = mlab.mesh(x, y, z, scalars=topo, colormap='gist_earth')

# Add a nice color bar
mlab.colorbar(surface, orientation='vertical')

# Add labels and title
mlab.xlabel('X')
mlab.ylabel('Y')
mlab.zlabel('Z')
mlab.title('Planet Earth')

# Show plot
mlab.show()