"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
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
