#!/usr/bin/python3
for i in range(ord('a'),ord('z')+1):
    if i in (ord('e'),ord('q')):
        continue
    else:
        print("{}".format(chr(i)),end="")
