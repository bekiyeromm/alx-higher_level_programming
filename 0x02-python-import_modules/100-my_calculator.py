#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    arg_count = len(argv)
    op = ["+", "-", "*", "/"]
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(0)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
