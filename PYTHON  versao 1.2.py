import scipy
print(scipy.__version__)

from scipy.integrate import quad
# Define the function to integrate
def f1(x):
    return x**2

def f2(x): 
    return x**3

def f3(x, a, b):
    return a*x**2 + b

    a= 2
    b= 1


# Calculate the integral from 0 to 1
result, error = quad(f1, 0, 1)

# Calculate the integral from 0 to 1
result, error = quad(f2, 0, 1)

# Calculate the integral from 0 to 1
result, error = quad(f3, 0, 1, args=(a,b))


# Print the result
print("O valor integral é:", result)

