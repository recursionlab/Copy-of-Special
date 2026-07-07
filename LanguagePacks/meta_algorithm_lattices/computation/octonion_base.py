"""
Octonion Computation for Pentagon Associator Classification
============================================================
This module implements octonion multiplication and associator computation
for the 5 bracketings of 4 elements.
"""

import numpy as np
from itertools import product

# Octonion multiplication table (Fano plane)
# Basis: 1, e1, e2, e3, e4, e5, e6, e7
# Indices: 0=1, 1=e1, 2=e2, 3=e3, 4=e4, 5=e5, 6=e6, 7=e7

# Fano plane lines (directed):
# e1*e2=e4, e2*e4=e1, e4*e1=e2
# e2*e3=e5, e3*e5=e2, e5*e2=e3
# e3*e4=e6, e4*e6=e3, e6*e3=e4
# e4*e5=e7, e5*e7=e4, e7*e4=e5
# e5*e6=e1, e6*e1=e5, e1*e6=e6? wait, let's be careful
# e6*e7=e2, e7*e2=e6, e2*e7=e7? 

# Standard Cayley-Dickson construction from quaternions:
# (a,b)(c,d) = (ac - d*b, da + bc*) where a,b,c,d are quaternions

# Let's use a well-tested octonion multiplication table
# Using the standard basis with Fano plane: 
# Lines: (e1,e2,e4), (e2,e3,e5), (e3,e4,e6), (e4,e5,e7), (e5,e6,e1), (e6,e7,e2), (e7,e1,e3)

OCT_MULT = np.zeros((8, 8, 8), dtype=int)

# Identity
for i in range(8):
    OCT_MULT[0, i, i] = 1
    OCT_MULT[i, 0, i] = 1

# Fano plane directed triads (cyclic order matters for signs)
# Each line (a,b,c) means a*b=c, b*c=a, c*a=b, and reverse products are negative
fano_lines = [
    (1, 2, 4),  # e1*e2=e4, e2*e4=e1, e4*e1=e2
    (2, 3, 5),  # e2*e3=e5, e3*e5=e2, e5*e2=e3
    (3, 4, 6),  # e3*e4=e6, e4*e6=e3, e6*e3=e4
    (4, 5, 7),  # e4*e5=e7, e5*e7=e4, e7*e4=e5
    (5, 6, 1),  # e5*e6=e1, e6*e1=e5, e1*e6=e6
    (6, 7, 2),  # e6*e7=e2, e7*e2=e6, e2*e7=e7
    (7, 1, 3),  # e7*e1=e3, e1*e3=e7, e3*e7=e1
]

for a, b, c in fano_lines:
    # Forward products
    OCT_MULT[a, b, c] = 1
    OCT_MULT[b, c, a] = 1
    OCT_MULT[c, a, b] = 1
    # Reverse products (anti-commutative for distinct imaginary units)
    OCT_MULT[b, a, c] = -1
    OCT_MULT[c, b, a] = -1
    OCT_MULT[a, c, b] = -1

# Squares of imaginary units are -1
for i in range(1, 8):
    OCT_MULT[i, i, 0] = -1

def octonion_mult(x, y):
    """Multiply two octonions x and y (8D vectors)."""
    result = np.zeros(8)
    for i in range(8):
        for j in range(8):
            if x[i] != 0 and y[j] != 0:
                k = np.where(OCT_MULT[i, j] != 0)[0]
                if len(k) > 0:
                    result[k[0]] += x[i] * y[j] * OCT_MULT[i, j, k[0]]
    return result

def associator(x, y, z):
    """Compute [x,y,z] = (xy)z - x(yz)"""
    xy = octonion_mult(x, y)
    yz = octonion_mult(y, z)
    left = octonion_mult(xy, z)
    right = octonion_mult(x, yz)
    return left - right

def octonion_to_str(oct_vec):
    """Convert octonion to readable string."""
    terms = []
    if abs(oct_vec[0]) > 1e-10:
        terms.append(f"{oct_vec[0]:.2f}")
    for i in range(1, 8):
        if abs(oct_vec[i]) > 1e-10:
            terms.append(f"{oct_vec[i]:.2f}e{i}")
    return " + ".join(terms) if terms else "0"

# Test basic octonion properties
print("=== Octonion Multiplication Tests ===")
e1 = np.zeros(8); e1[1] = 1
e2 = np.zeros(8); e2[2] = 1
e4 = np.zeros(8); e4[4] = 1

print(f"e1 * e2 = {octonion_to_str(octonion_mult(e1, e2))}")  # should be e4
print(f"e2 * e4 = {octonion_to_str(octonion_mult(e2, e4))}")  # should be e1
print(f"e4 * e1 = {octonion_to_str(octonion_mult(e4, e1))}")  # should be e2
print(f"e2 * e1 = {octonion_to_str(octonion_mult(e2, e1))}")  # should be -e4

# Test alternativity: x(xy) = x^2 y and (xy)y = x y^2
x = np.array([1, 2, 0, 1, 0, 0, 0, 0])  # 1 + 2e1 + e3
y = np.array([0, 1, 1, 0, 0, 1, 0, 0])  # e1 + e2 + e5

xy = octonion_mult(x, y)
x_xy = octonion_mult(x, xy)
xx = octonion_mult(x, x)
xx_y = octonion_mult(xx, y)
print(f"\nAlternativity check x(xy) vs x^2y:")
print(f"  x(xy) = {octonion_to_str(x_xy)}")
print(f"  x^2 y = {octonion_to_str(xx_y)}")
print(f"  Equal? {np.allclose(x_xy, xx_y)}")

# Test associator non-zero
assoc = associator(x, y, x)
print(f"\nAssociator [x,y,x] = {octonion_to_str(assoc)}")
print(f"  Non-zero? {not np.allclose(assoc, 0)}")