"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/AnaisM7/lab11-AM-EB.git
# Partner 1: Anais Maldonado
# Partner 2: Emy Bijoy

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
   try:
       if a < 0:
          raise ValueError("Cannot compute sqrt of a negative number")
       return math.sqrt(a)
   except ValueError as e:
       print(f"Error in square_root: {e}")
       return None


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error in hypotenuse: {e}")
        return None

