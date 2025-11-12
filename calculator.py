# https://github.com/AnaisM7/lab11-AM-EB.git
# Partner 1: Anais Maldonado
# Partner 2: Emy Bijoy

import math

<<<<<<< HEAD
# First example
def add(a, b): 
=======
def add(a, b):
>>>>>>> b257e6e8d93e746eef00ad91c9da15cb970ce940
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
<<<<<<< HEAD
        return None
=======
        return None

>>>>>>> b257e6e8d93e746eef00ad91c9da15cb970ce940
