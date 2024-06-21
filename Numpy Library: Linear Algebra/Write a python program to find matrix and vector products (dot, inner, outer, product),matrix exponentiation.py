# Python Program illustrating numpy.inner() method
import numpy as np

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Inner Product of Vectors
print("\nInner product of vectors a and b =")
print(np.inner(a, b))
print("---------------------------------------")

# Outer product of vectors
print("\nOuter product of vectors a and b =")
print(np.outer(a, b))
print("---------------------------------------")

# Cross product of vectors
print("\nCross product of vectors a and b =")
print(np.cross(a, b))