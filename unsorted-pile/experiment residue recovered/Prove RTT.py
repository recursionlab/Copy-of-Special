import sys
sys.path.append(r"C:\Users\ANN\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages")

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1 - 0.5 * x
tau = lambda x: abs(f(x) - x)

x_vals = [0]
tau_vals = []

for i in range(100):
    x = f(x_vals[-1])
    x_vals.append(x)
    tau_vals.append(tau(x))

plt.plot(tau_vals, label="τ (torsion)")
plt.axhline(y=0.1, color='r', linestyle='--', label="τ* threshold")
plt.xlabel("Iteration")
plt.ylabel("Torsion τ")
plt.legend()
plt.show()