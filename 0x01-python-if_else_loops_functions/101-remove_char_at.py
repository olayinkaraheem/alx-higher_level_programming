#!/usr/bin/python3
def remove_char_at(str, n):
    out_str = ""
    for ind in range(len(str)):
        if n >= 0 and n == ind:
            out_str += ""
        else:
            out_str += str[ind]
    return out_str
