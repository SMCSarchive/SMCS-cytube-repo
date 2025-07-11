import numpy as np
import matplotlib.pyplot as plt

# Generate 2D Sierpinski carpet to approximate fractal structure
def sierpinski_carpet(n, size=1):
    grid = np.ones((3**n, 3**n))  # Initialize solid square
    for i in range(n):
        step = 3**(n - i - 1)
        for x in range(0, 3**n, 3*step):
            for y in range(0, 3**n, 3*step):
                grid[x + step:x + 2*step, y + step:y + 2*step] = 0  # Remove central square
    return grid

# Plot parameters
n = 4  # Number of fractal iterations (adjust for detail)
R = 4.4e26  # Observable universe radius (~46.5 billion light-years, in meters)
grid = sierpinski_carpet(n)

# Create plot
plt.figure(figsize=(8, 8))
plt.imshow(grid, cmap='gray', extent=[-1, 1, -1, 1])  # Normalized coordinates
plt.scatter([0], [0], color='red', s=100, label='Earth')  # Earth at (0,0)
plt.title("2D Projection of Universe: Homogeneous Core, Fractal Boundary")
plt.xlabel("X (normalized, x/R)")
plt.ylabel("Y (normalized, y/R)")
plt.legend()
plt.grid(False)  # Disable grid for clarity
plt.show()