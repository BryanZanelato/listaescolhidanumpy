import numpy as np

array = np.random.rand(20)

media = np.mean(array)
desvio_padrao = np.std(array)
valor_maximo = np.max(array)
valor_minimo = np.min(array)

print(f"Média: {media:.4f}")
print(f"Desvio Padrão: {desvio_padrao:.4f}")
print(f"Valor Máximo: {valor_maximo:.4f}")
print(f"Valor Mínimo: {valor_minimo:.4f}")
