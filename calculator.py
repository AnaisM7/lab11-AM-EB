"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

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


def add(a, b):
    a+b

def sub(a, b):
    a-b

def mul(a, b):
    a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    b/a

def log(a, b):
    math.log(b, a)

def exp(a, b):
    a**b
