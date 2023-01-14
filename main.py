# Author: Adam Peters
# Date: 1/13/2023
# Program: Horner's Algorithm
# ------------------------------
# Description: A simple algorithm that breaks down polynomials
# to avoid having to power them to the nth power

#
high_poly = int(input("What is the value of the highest polynomial? "))

equation_str = ""
equation = []
for i in range(high_poly, 0, -1):
    poly_coef = int(input("What is the coefficient of the " + str(i) + "th polynomial? "))
    equation_str += str(poly_coef) + "x^" + str(i) + " + "
    equation.append(poly_coef)

constant = int(input("What is the constant, 0 if none? "))
equation_str += str(constant)
equation.append(constant)


print(equation_str)
print(equation)

x = int(input("What does x equal? "))
s = equation[0]
for i in range(1, len(equation)):
    s = (s * x) + equation[i]

print(s)
