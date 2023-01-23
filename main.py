# Author: Adam Peters
# Date: 1/13/2023
# Program: Horner's Algorithm
# ------------------------------
# Description: A simple algorithm that breaks down polynomials
# to avoid having to power them to the nth power

# TO DO
# Format Execution Time in a Meaningful Way
# Graph the Execution Time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import timeit
import time


# Gets the polynomial equation from the user
def get_polynomial_eq():
    # Initialize Coefficient List to Return
    eq = []

    # Prompt the user for number of polynomials
    # which we will use to determine how many coefficients we need
    high_poly = int(input("What is the value of the highest polynomial? "))

    # Get the user's inputs for each coefficient
    # and add them to our equation string and list

    for i in range(high_poly, 0, -1):
        poly_coef = int(input("What is the coefficient of the " + str(i) + "th polynomial? "))
        eq.append(poly_coef)

    # Finally, add the end constant
    constant = int(input("What is the constant, 0 if none? "))
    eq.append(constant)

    return eq


# Generates the Polynomial String based on the List of Coefficients
def get_polynomial_string(eq):
    # Initialize String to Return
    eq_str = ""

    # Add each Coefficient and Power to the String
    for i in range(len(eq) - 1):
        eq_str += str(eq[i]) + "x^" + str(len(eq) - (i + 1)) + " + "

    # Add the Consonant to the End of the String
    eq_str += str(eq[len(eq) - 1])

    return eq_str


# Different Methods for Solving the Polynomial

# Traditional Power Method, Done Recursively
# Time Complexity: O(n)
def power(x, n):
    # Base Case, x^0 = 1
    if n == 0:
        return 1

    # If x = 0, x^n = 0
    if x == 0:
        return 0

    return x * power(x, n - 1)


# Optimized Power Method, Divide and Conquer
# Equivalent Time and Space Complexity to Python's pow() func
# Time Complexity O(log|n|)
# Space Complexity: O(1)
def opt_power(x, n):
    temp = 0

    # Base Case, x^0 = 1
    if n == 0:
        return 1

    temp = opt_power(x, int(n / 2))

    if n % 2 == 0:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


# Horner's Algorithm
# Time Complexity: O(n)
def horner(coefs, sol):
    # Initializing the first coefficient
    r = coefs[0]

    # Evaluating the Polynomial with Horner's Method
    # https://en.wikipedia.org/wiki/Horner%27s_method
    for i in range(1, len(coefs)):
        r = (r * sol) + equation[i]

    return r


# Solution to polynomial using the power method above
def solve_poly_trad(coefs, sol):
    # Initialize a total
    total = 0

    # Multiple each coefficient by the power of solution (x) to the corresponding power (len(equation) - (i + 1))
    # Add it to the total
    for i in range(len(coefs)):
        total += coefs[i] * power(sol, len(coefs) - (i + 1))

    return total


# Solution to polynomial using the opt_power method above
def solve_poly_opt(coefs, sol):
    # Initialize a total
    total = 0

    # Multiple each coefficient by the power of solution (x) to the corresponding power (len(equation) - (i + 1))
    # Add it to the total
    for i in range(len(coefs)):
        total += coefs[i] * opt_power(sol, len(coefs) - (i + 1))

    return total


# Start of the Program
print("We are going to examine three ways to solve a polynomial equation")
print("You can either use one of the provided polynomials or enter your own")
print("1: 3x^2 + 2x + 1")
print("2: Enter your own")

choice = int(input(": "))

equation = []
equation_str = ""

if choice == 1:
    equation = [3, 2, 1]
    equation_str = "3x^2 + 2x^1 + 1"
elif choice == 2:
    equation = get_polynomial_eq()
    equation_str = get_polynomial_string(equation)

print(equation_str)
print(equation)

# Receives the value of x to plug into Horner's Algorithm
solution = int(input("What does x equal? "))

# Create a Space
print()

# Answer to each Method
# Should be the same
print("Solving using Traditional Power Method...")
print(solve_poly_trad(equation, solution))
print(timeit.timeit(stmt="solve_poly_trad(equation, solution)",
                    setup="",
                    number=1000,
                    globals=globals()))

print("Solving using Optimized Power Method...")
print(solve_poly_opt(equation, solution))
print(timeit.timeit(stmt="solve_poly_trad(equation, solution)",
                    setup="",
                    number=1000,
                    globals=globals()))

print("Solving using Horner's Algorithm...")
print(horner(equation, solution))
print(timeit.timeit(stmt="solve_poly_trad(equation, solution)",
                    setup="",
                    number=1000,
                    globals=globals()))
