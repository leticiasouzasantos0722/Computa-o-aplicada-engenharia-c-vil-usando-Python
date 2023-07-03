import scipy
import math
import numpy as np
from scipy.integrate import quad
from numpy import sqrt, sin, cos, pi
import matplotlib.pyplot as plt 

print(scipy.__version__)
print(math.pi)

# Defina as funções para integral

def f1(x):
     return x**2

def f2(x): 
     return x**3

def f3(x, a, b): 
     return a*x**2 + b

def f4(x, c): 
     return (sqrt(c**2 - x**2) / c)**2

def f5(x, d): 
     return (d*cos(x))

# usuario define os valores de a e b para f3
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

# usuario define o valor de c para f4
c = float(input("Enter the value for c: "))

#  usuario define o valor de d para f5
d = float(input("Enter the value for d: "))

# Calcular as integrais
result1, error1 = quad(f1, 0, 1)
result2, error2 = quad(f2, 0, 1)
result3, error3 = quad(f3, 0, 1, args=(a, b))
result4, error4 = quad(f4, -6, 6, args=(c))
result5, error5 = quad(f5, 0, (pi / 2), args=(d))

# Print os resultados
print("The integral value for f1 is:", result1)
print("The integral value for f2 is:", result2)
print("The integral value for f3 is:", result3)
print("The integral value for f4 is:", result4)
print("The integral value for f5 is:", result5)

# Plot tas funções
x = np.linspace(0, 1, 400)
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x, f1(x), color='black')
plt.title('Função 1')

plt.subplot(2, 3, 2)
plt.plot(x, f2(x))
plt.title('Função 2')


plt.subplot(2, 3, 3)
plt.plot(x, f3(x, a, b))
plt.title('Função 3')

x = np.linspace(-6, 6, 400)
plt.subplot(2, 3, 4)
plt.plot(x, f4(x, c))
plt.title('Função 4')

x = np.linspace(0, np.pi/2, 400)
plt.subplot(2, 3, 5)
plt.plot(x, f5(x, d))
plt.title('Função 5')

plt.tight_layout()
plt.show()