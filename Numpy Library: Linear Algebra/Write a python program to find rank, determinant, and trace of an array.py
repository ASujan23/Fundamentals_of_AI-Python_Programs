import numpy as np
my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3]])
print("Matrix")
for row in my_matrix:
    print(row)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank)

#determinant
import numpy as np
a = np.array([[1,2],[3,4]])
print("Original array:")
print(a)
result = np.linalg.det(a)
print("Determinant of the said array:")
print(result)

#trace
import numpy as np
# Let's create a square matrix (NxN matrix)
mx = np.array([[1,1,1],[0,1,2],[1,5,3]])
# Let's get trace(sum of diagonal elements)
print(mx.trace())