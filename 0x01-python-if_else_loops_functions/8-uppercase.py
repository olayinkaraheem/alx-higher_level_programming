#!/usr/bin/python3
def uppercase(str):
    out_str = ""
    for ind in range(len(str)):
        if ord(str[ind]) in range(97, 123):
            out_str += chr(ord(str[ind]) - 32)
        else:
            out_str += str[ind]

    print("{}".format(out_str))
