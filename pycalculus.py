import sympy as sp
from sympy import *
import argparse
#e = Symbol('e')

# Command Line Argument Setup
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--derivative', required=False, metavar="FUNCTION")
parser.add_argument('-i','--integral', required=False, metavar="INTEGRAL")

# lower limit, upper limit
parser.add_argument('-l', '--limits', required=False, nargs='+',metavar="(lower_limit, upper_limit")
args = parser.parse_args()

init_printing(use_unicode=False, wrap_line=False, no_global=True)
x,y = symbols('x y')

def Take_Derivative(expression):

    expression_derivative = Derivative(expression, x)
    return expression_derivative

def Take_Indefinite_Integral(expression):

    expression_integral = sp.integrate(expression)
    return expression_integral

def Take_Definite_Integral(expression, limits):

    expression_integral = integrate(expression, ('x',limits))
    return expression_integral

try:
    if args.derivative is not None:
        result = Take_Derivative(args.derivative)
        print(result)

    elif args.integral is not None and args.limits is not None:
        result = Take_Definite_Integral(args.integral,args.limits)
        print(result)

    elif args.integral is not None and args.limits is None:
        result = Take_Indefinite_Integral(args.integral)
        print(result)
except Exception as e:
    print(e)
