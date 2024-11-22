import numpy as np

matrix = np.array([[2, 0], [0, 3]])
v = np.array([1, 2])
transformed_v = np.dot(matrix, v)

print(transformed_v)
