
import scipy
import math
import numpy as np
from scipy.integrate import quad
from numpy import sqrt, sin, cos, pi

print(scipy.__version__)
print(math.pi)

# Define the function to integrate
def f1(x): return x**2
def f2(x): return x**3
def f3(x, a, b): return a*x**2 + b
def f4(x, c): return sqrt(c**2 - x**2) / c
def f5(x, d): return (d*cos(x))

# Get the values of a and b for f3 from the user
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

# Get the value of c for f4 from the user
c = float(input("Enter the value for c: "))

# Get the value of d for f5 from the user
d = float(input("Enter the value for d: "))

# Calculate the integrals
result1, error1 = quad(f1, 0, 1)
result2, error2 = quad(f2, 0, 1)
result3, error3 = quad(f3, 0, 1, args=(a, b))
result4, error4 = quad(f4, -6, 6, args=(c))
result5, error5 = quad(f5, 0, (pi / 2), args=(d))

# Print the results
print("The integral value for f1 is:", result1)
print("The integral value for f2 is:", result2)
print("The integral value for f3 is:", result3)
print("The integral value for f4 is:", result4)
print("The integral value for f5 is:", result5)
