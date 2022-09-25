#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arg_count = len(sys.argv) - 1
    for ind in range(1, len(sys.argv)):
        sum += int(sys.argv[ind])
    print("{}".format(sum))
