# Author: Adam Peters
# Date: 1/13/2023
# Program: Horner's Algorithm
# ------------------------------
# Description: A simple algorithm that breaks down polynomials
# to avoid having to power them to the nth power

# Prompt the user for number of polynomials
# which we will use to determine how many coefficients we need
high_poly = int(input("What is the value of the highest polynomial? "))

# Get the user's inputs for each coefficient
# and add them to our equation string and list
equation_str = ""
equation = []
for i in range(high_poly, 0, -1):
    poly_coef = int(input("What is the coefficient of the " + str(i) + "th polynomial? "))
    equation_str += str(poly_coef) + "x^" + str(i) + " + "
    equation.append(poly_coef)

# Finally, add the end constant
constant = int(input("What is the constant, 0 if none? "))
equation_str += str(constant)
equation.append(constant)

print(equation_str)
print(equation)

x = int(input("What does x equal? "))

# Horner's Algorithm O(n)
s = equation[0]
for i in range(1, len(equation)):
    s = (s * x) + equation[i]

print("Horner's Algorithm: ")
print(s)

# TO DO
# Add time and memory tracking with timeit and memory_profiler
# Add original power method solution and solution using optimized power method

# def power(n, p):
#     for k in range(1, p):
#         n = n * n
#     return n


# Solving with the traditional method O(n^2)
# print(power(2, 3))

