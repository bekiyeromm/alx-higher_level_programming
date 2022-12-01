#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_count = len(argv)
    i = 1
    if arg_count == 0:
        print("{:d} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{:d} argument:".format(arg_count))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(arg_count))
        while i <= arg_count:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i = i + 1
