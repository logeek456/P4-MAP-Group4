import numpy as np
import numba as nb
from mayavi import mlab


def generate_topography():
    file = open("topography_data.txt", "w")
    for i in range(100):
        for j in range(50):
            file.write(str(np.random.randint(0,8000)) + " ")
        file.write("\n")
    file.close()

generate_topography()

#Generate a 100x50 .txt file for the topography. Needs to have an ocean (defined by height 0), a couple islands (height > 10) and a continent (height > 10) with a few mountains (height > 2000). Max height is 8000, and it should be continuous






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