import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
outer_product = np.outer(a, b)

print("Produto escalar:", dot_product)
print("Produto externo:\n", outer_product)
