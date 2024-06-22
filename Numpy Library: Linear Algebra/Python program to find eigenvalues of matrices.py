from numpy.linalg import eig
import numpy as np
a=np.array([[10,20,30,40],[1,2,3,5],[7,8,9,10],[15,25,35,45]])
values , vectors = eig(a)
print(values)

print(vectors)