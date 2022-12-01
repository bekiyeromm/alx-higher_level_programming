#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv=sys.argv[1:]
    arg_count = len(argv)
    i = 1
    sum = 0
    while i <= arg_count:
        sum = sum + int(sys.argv[i])
        i = i + 1
    print("{:d}".format(sum))
