#!/usr/bin/python3
for ind in range(122, 96, -1):
    print("{}".format(chr(ind - 32) if ind % 2 == 1 else chr(ind)), end="")
