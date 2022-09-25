#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    print("{} {}".format(
            num_args,
            "arguments:" if num_args > 1
            else (
                "argument:" if num_args == 1
                else "argument."
            )
        )
    )
    for arg_ind in range(1, num_args + 1):
        print("{}: {}".format(arg_ind, sys.argv[arg_ind]))
