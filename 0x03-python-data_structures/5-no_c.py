#!/usr/bin/python3
def no_c(my_string):
    output_string = ""
    for char in my_string:
        if ord(char) not in [99, 67]:
            output_string += char
    return output_string
