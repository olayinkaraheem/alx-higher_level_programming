#!/usr/bin/python3
for first_dig in range(0, 10):
    for second_dig in range(0, 10):
        if first_dig != second_dig and first_dig < second_dig:
            if second_dig == 9 and first_dig == second_dig - 1:
                print("{}{}".format(first_dig, second_dig))
            else:
                print("{}{}".format(first_dig, second_dig), end=", ")
