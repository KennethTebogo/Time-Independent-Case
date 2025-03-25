---

# 1D Particle in a Box - Solving the Schrödinger Equation

This project solves the **time-independent Schrödinger equation** for a particle confined in a **1D infinite potential well** using the **finite difference method**. The solution calculates the energy eigenvalues and wavefunctions for the system and visualizes the probability densities for the first few energy levels.

---

## **Table of Contents**

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

---

## **Description**

This repository contains a Python implementation that numerically solves the time-independent Schrödinger equation for a particle in a 1D box (infinite square well potential). The solution is done using the finite difference method for discretizing the differential equation into a matrix eigenvalue problem.

The energy eigenvalues and wavefunctions are computed and visualized, showing the first few eigenstates and their corresponding probability densities.

---

## **Installation**

To run the code, you need Python and the required libraries. The easiest way to install the necessary dependencies is by using `pip`.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KennethTebogo/1d-particle-in-a-box.git
   cd 1d-particle-in-a-box
   ```

2. **Install the dependencies:**

   You can install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually:

   ```bash
   pip install numpy matplotlib
   ```

---

## **Usage**

After installing the necessary libraries, you can run the script to calculate and visualize the wavefunctions and energy eigenvalues.

1. **Run the script:**

   ```bash
   python solve_schrodinger.py
   ```

2. **Output:**

   [Wavefunctions Plot](./trinket_plot.png)

---

## **Code Explanation**

### Key Steps in the Code:

1. **Initialization and Parameters:**
   - The length of the box \(L\) and the number of grid points \(N\) are set, along with the spatial grid.
   
2. **Kinetic Energy Operator:**
   - A finite difference method is used to approximate the second derivative in the kinetic energy term of the Schrödinger equation.

3. **Potential Energy:**
   - The potential energy is set to zero inside the box, which represents an infinite square well potential.

4. **Hamiltonian Matrix:**
   - The Hamiltonian matrix is created by adding the kinetic and potential energy matrices. This matrix represents the total energy operator of the system.

5. **Eigenvalue Problem:**
   - The eigenvalues (energy levels) and eigenvectors (wavefunctions) are calculated by solving the matrix eigenvalue problem.

6. **Visualization:**
   - The first few wavefunctions (probability densities) are plotted to visualize the standing wave patterns and their corresponding energy levels.

### Dependencies:

- **NumPy**: For numerical calculations and matrix manipulations.
- **Matplotlib**: For plotting the wavefunctions and energy levels.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and adapt the `README.md` to your specific needs and include any additional information as necessary!
