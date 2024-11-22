import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.linspace(0, 10, 20)
ruido = np.random.normal(0, 2, size=x.shape)
y = 2 * x + 3 + ruido

X = np.vstack([x, np.ones_like(x)]).T
coeficientes = np.linalg.inv(X.T @ X) @ X.T @ y

a, b = coeficientes
coef_polyfit = np.polyfit(x, y, 1)
a_polyfit, b_polyfit = coef_polyfit

print(f"Coeficientes (álgebra matricial): a = {a:.2f}, b = {b:.2f}")
print(f"Coeficientes (numpy.polyfit): a = {a_polyfit:.2f}, b = {b_polyfit:.2f}")

plt.scatter(x, y, label="Dados", color='blue')
plt.plot(x, a * x + b, label=f'Regressão Linear (método matricial)', color='red')
plt.plot(x, a_polyfit * x + b_polyfit, label=f'Regressão Linear (polyfit)', color='green', linestyle='--')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão Linear - Comparação")
plt.show()
