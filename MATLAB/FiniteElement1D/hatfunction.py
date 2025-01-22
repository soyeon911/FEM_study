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
