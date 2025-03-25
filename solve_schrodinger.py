import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the box
N = 100  # Number of grid points
dx = L / N  # Grid spacing
x = np.linspace(0, L, N)  # Position grid

# Kinetic energy operator (finite difference)
T = -0.5 * (np.diag(np.ones(N-1), 1) - 2 * np.diag(np.ones(N), 0) + np.diag(np.ones(N-1), -1)) / dx**2

# Potential energy (infinite square well)
V = np.zeros(N)  # Zero potential inside the box

# Hamiltonian
H = T + np.diag(V)

# Solve for eigenvalues and eigenvectors
energies, wavefunctions = np.linalg.eigh(H)

# Plot the first few eigenfunctions
plt.figure(figsize=(8, 6))
for i in range(3):  # First three eigenfunctions
    plt.plot(x, wavefunctions[:, i]**2, label=f'E = {energies[i]:.2f}')
plt.xlabel('Position (x)')
plt.ylabel('Probability Density')
plt.title('Wavefunctions of a Particle in a Box')
plt.legend()
plt.show()
