import numpy as np
my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3]])
print("Matrix")
for row in my_matrix:
    print(row)

rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank)

# Determinant:
import numpy as np
n_array = np.array([[50, 29], [30, 44]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)
print("\nDeterminant of given 2X2 matrix:")
print(int(det))

# Trace:
import numpy as np
# make matrix with numpy
mx = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
# applying matrix.trace() method
MatrixTrace = mx.trace()
print(MatrixTrace)