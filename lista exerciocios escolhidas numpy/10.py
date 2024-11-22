import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) 
alturas = np.random.normal(170, 10, 100)

percentil_25 = np.percentile(alturas, 25)
percentil_50 = np.percentile(alturas, 50) 
percentil_75 = np.percentile(alturas, 75)

acima_180 = np.sum(alturas > 180)

print(f"Percentil 25: {percentil_25:.2f}")
print(f"Mediana (Percentil 50): {percentil_50:.2f}")
print(f"Percentil 75: {percentil_75:.2f}")
print(f"Quantidade de pessoas com altura acima de 180 cm: {acima_180}")

plt.hist(alturas, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribuição de Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
