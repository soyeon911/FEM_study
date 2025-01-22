# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jQoHMLjbiWkaXY9A_zdIaDBOLgG-OT99
"""

import numpy as np
import matplotlib.pyplot as plt

def hat_function_piecewise(x, xi, hi_minus1, hi_plus1):

    if xi - hi_minus1 <= x <= xi:
        return (x - (xi - hi_minus1)) / hi_minus1
    elif xi <= x <= xi + hi_plus1:
        return ((xi + hi_plus1) - x) / hi_plus1
    else:
        return 0


nodes = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
h = 0.2


x_values = np.linspace(0, 1, 500)


plt.figure(figsize=(10, 6))
for i in range(1, len(nodes) - 1):  # Exclude boundary nodes for simplicity
    y_values = [hat_function_piecewise(x, nodes[i], h, h) for x in x_values]
    plt.plot(x_values, y_values, label=f'$\phi_{i}$')


plt.title("Hat Functions for Uniform Mesh Intervals", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$\phi_i(x)$", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Hat Functions", fontsize=10)
plt.show()

########################################################################################

nodes = np.array([0, 0.33, 0.66, 1.0])
h = 0.3
plt.figure(figsize=(10, 6))
for i in range(1, len(nodes) - 1):  # Exclude boundary nodes for simplicity
    y_values = [hat_function_piecewise(x, nodes[i], h, h) for x in x_values]
    plt.plot(x_values, y_values, label=f'$\phi_{i}$')


plt.title("Hat Functions for Uniform Mesh Intervals", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$\phi_i(x)$", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Hat Functions", fontsize=10)
plt.show()


########################################################################################

nodes = np.array([0, 0.4, 0.5, 0.75, 1.0])
h = 0.4
plt.figure(figsize=(10, 6))
for i in range(1, len(nodes) - 1):  # Exclude boundary nodes for simplicity
    y_values = [hat_function_piecewise(x, nodes[i], h, h) for x in x_values]
    plt.plot(x_values, y_values, label=f'$\phi_{i}$')


plt.title("Hat Functions for Uniform Mesh Intervals", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$\phi_i(x)$", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Hat Functions", fontsize=10)
plt.show()

########################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Define hat function based on piecewise definition
def hat_function_piecewise(x, xi, hi_minus1, hi_plus1):
    if xi - hi_minus1 <= x <= xi:
        return (x - (xi - hi_minus1)) / hi_minus1
    elif xi <= x <= xi + hi_plus1:
        return ((xi + hi_plus1) - x) / hi_plus1
    else:
        return 0

# Function to plot hat functions for a given interval size h
def plot_hat_functions(h, ax):
    # Define nodes based on the interval size h
    nodes = np.arange(0, 1 + h, h)
    x_values = np.linspace(0, 1, 500)  # Continuous range for plotting

    # Plot hat functions for each interior node
    for i in range(1, len(nodes) - 1):  # Exclude boundary nodes
        y_values = [hat_function_piecewise(x, nodes[i], h, h) for x in x_values]
        ax.plot(x_values, y_values, label=f'$\phi_{{{i}}}$')

    # Customize plot
    ax.set_title(f"Hat Functions (h = {h})", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("$\phi_i(x)$", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(title="Hat Functions", fontsize=10)

# Create subplots for different h values
h_values = [1/4, 1/3, 1/5, 1/7]  # Different interval sizes
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot for each h value
for ax, h in zip(axes.flatten(), h_values):
    plot_hat_functions(h, ax)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

########################################################################################

import numpy as np

def stiffness_matrix(nodes, a):
    """
    Compute the stiffness matrix for a given set of nodes and coefficient function a(x).

    Parameters:
        nodes: array-like
            Coordinates of the nodes.
        a: function
            Coefficient function a(x) for the stiffness matrix.

    Returns:
        A: 2D numpy array
            The stiffness matrix.
    """
    n = len(nodes) - 1  # Number of intervals
    A = np.zeros((n + 1, n + 1))  # Initialize the stiffness matrix

    for i in range(n):
        h = nodes[i + 1] - nodes[i]  # Interval length
        x_mid = (nodes[i] + nodes[i + 1]) / 2  # Midpoint of the interval
        a_mid = a(x_mid)  # Evaluate a(x) at the midpoint

        # Local stiffness matrix
        local_A = (a_mid / h) * np.array([[1, -1], [-1, 1]])

        # Add the local stiffness matrix to the global matrix
        A[i:i + 2, i:i + 2] += local_A

    return A

# Example coefficient function a(x)
def coefficient_a(x):
    return 1  # Constant coefficient (e.g., a(x) = 1)

# Define h values and compute stiffness matrices
h_values = [1/4, 1/3, 1/5, 1/7]  # Different interval sizes

for h in h_values:
    # Generate nodes for the given h
    nodes = np.arange(0, 1 + h, h)

    # Compute the stiffness matrix
    A = stiffness_matrix(nodes, coefficient_a)

    # Print results
    print(f"Stiffness Matrix for h = {h}:")
    print(A)
    print("-" * 40)

########################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Define piecewise linear hat functions for the boundary and interior nodes
def hat_function(x, xi, xi_minus1=None, xi_plus1=None):
    if xi_minus1 is None:  # Left boundary node
        return np.maximum(0, (xi_plus1 - x) / (xi_plus1 - xi))
    elif xi_plus1 is None:  # Right boundary node
        return np.maximum(0, (x - xi_minus1) / (xi - xi_minus1))
    else:  # Interior node
        return np.maximum(0, np.minimum((x - xi_minus1) / (xi - xi_minus1), (xi_plus1 - x) / (xi_plus1 - xi)))

# Define nodes
nodes = np.array([0, 0.25, 0.5, 0.75, 1.0])  # Uniform intervals
x_values = np.linspace(0, 1, 500)

# Plot the hat functions
plt.figure(figsize=(10, 6))

# Left boundary node
y_left = [hat_function(x, nodes[0], xi_plus1=nodes[1]) for x in x_values]
plt.plot(x_values, y_left, label="$\phi_0(x)$ (Left boundary)")

# Interior nodes
for i in range(1, len(nodes) - 1):
    y_interior = [hat_function(x, nodes[i], nodes[i-1], nodes[i+1]) for x in x_values]
    plt.plot(x_values, y_interior, label=f"$\phi_{i}(x)$ (Interior)")

# Right boundary node
y_right = [hat_function(x, nodes[-1], xi_minus1=nodes[-2]) for x in x_values]
plt.plot(x_values, y_right, label="$\phi_n(x)$ (Right boundary)")

# Customize plot
plt.title("Hat Functions with Boundary and Interior Nodes", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$\phi(x)$", fontsize=12)
plt.legend(title="Node", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()