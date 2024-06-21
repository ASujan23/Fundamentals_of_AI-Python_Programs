"""
Python program for indexing using basic slicing with ellipsis(Ellipsis can also be used along
with basic slicing. Ellipsis (...) is the number of : objects needed to make a selection tuple of
the same length as the dimensions of the array.)
"""
import numpy as np

# A 3 dimensional array.
b = np.array([[[1, 2, 3],[4, 5, 6]],
[[7, 8, 9],[10, 11, 12]]])

print(b[...,1]) #Equivalent to b[: ,: ,1 ]

# Python program showing advanced indexing
import numpy as np
a = np.array([[1 ,2 ],[3 ,4 ],[5 ,6 ]])
print(a[[0 ,1 ,2 ],[0 ,0 ,1]])

# You may wish to select numbers greater than 50
import numpy as np
a = np.array([10, 40, 80, 50, 100])
print(a[a>50])

# You may wish to select those elements whose sum of row is a multiple of 10.
import numpy as np
b = np.array([[5, 5],[4, 5],[16, 4]])
sumrow = b.sum(-1)
print(b[sumrow%10==0])