#!/usr/bin/python3
for char_code in range(97, 123):
    if chr(char_code) not in ('e', 'q'):
        print("{}".format(chr(char_code)), end="")
