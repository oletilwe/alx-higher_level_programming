#!/usr/bin/python3
from calculator_1.py import add, subtract, multiply, divide
a = 10
b = 5
addition_result = add(a, b)
subtraction_result = subtract(a, b)
multiplication_result = multiply(a, b)
division_result = divide(a, b)
result = f"{a} + {b} = {addition_result}, {a} - {b} = {subtraction_result}, {a} * {b} = {multiplication_result}, {a} / {b} = {division_result}"
