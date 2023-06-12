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

# Define the values of a and b for f3
a = 2
b = 1

# Calculate the integral from 0 to 1
result1, error1 = quad(f1, 0, 1)

# Calculate the integral from 0 to 1
result2, error2 = quad(f2, 0, 1)

# Calculate the integral from 0 to 1
result3, error3 = quad(f3, 0, 1, args=(a,b))


# Print the results
print("The integral value for f1 is:", result1)
print("The integral value for f2 is:", result2)
print("The integral value for f3 is:", result3)
