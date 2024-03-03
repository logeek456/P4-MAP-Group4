import numpy as np
import pyvista as pv

def _cell_bounds(points, bound_position=0.5):
    """
    Calculate coordinate cell boundaries.

    Parameters
    ----------
    points: numpy.ndarray
        One-dimensional array of uniformly spaced values of shape (M,).

    bound_position: bool, optional
        The desired position of the bounds relative to the position
        of the points.

    Returns
    -------
    bounds: numpy.ndarray
        Array of shape (M+1,)
    """
    if points.ndim != 1:
        raise ValueError("Only 1D points are allowed.")
    diffs = np.diff(points)
    delta = diffs[0] * bound_position
    bounds = np.concatenate([[points[0] - delta], points + delta])
    return bounds

# Fonction à utiliser pour colorier la sphère
def f(x, y):
    return np.cos(2*np.pi*x/360)*np.cos(2*np.pi*y/360)

# Approximate radius of the Earth
RADIUS = 1

# Longitudes and latitudes
x = np.linspace(0, 360, 1000)
y = np.linspace(-90, 90, 1000)
y_polar = 90.0 - y  # grid_from_sph_coords() expects polar angle

xx, yy = np.meshgrid(x, y)

# Évaluation de la fonction f aux coordonnées (x, y)
scalar = f(xx, yy)

# Create arrays of grid cell boundaries, which have shape of (x.shape[0] + 1)
xx_bounds = _cell_bounds(x)
yy_bounds = _cell_bounds(y_polar)
# Vertical levels
# in this case a single level slightly above the surface of a sphere
levels = [RADIUS * 1.01]

grid_scalar = pv.grid_from_sph_coords(xx_bounds, yy_bounds, levels)

# And fill its cell arrays with the scalar data
grid_scalar.cell_data["example"] = np.array(scalar).swapaxes(-2, -1).ravel("C")

# Make a plot
p = pv.Plotter()
p.add_mesh(pv.Sphere(radius=RADIUS))
p.add_mesh(grid_scalar, clim=[-1, 1], opacity=0.5, cmap="plasma")
p.show()
