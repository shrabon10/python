import math

def f(x):
    return math.exp(-x) - math.sin(x)

a = float(input("Enter the first initial guess: "))
b = float(input("Enter the second initial guess: "))

if f(a) * f(b) > 0:
    print("Bisection method fails. Choose different initial guesses.")
else:
    err = float('inf')
    n = 0
    while err > 0.0001:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        err = abs(a - b)
        n = n + 1
        print("Root =", c, "Iteration", n)
