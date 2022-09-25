#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    allowed_operators = ['*', '-', '+', '/']

    a = int(sys.argv[1])
    input_operator = sys.argv[2]
    b = int(sys.argv[3])

    if input_operator not in allowed_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if input_operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if input_operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if input_operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if input_operator == "*":
        print("{} / {} = {}".format(a, b, div(a, b)))
    exit(0)
