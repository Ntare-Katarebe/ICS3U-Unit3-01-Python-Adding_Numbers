#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program adds up two numbers together
#    with numbers inputted from the user

import math


def main():
    # This function adds up two numbers together

    # input
    print("This program adds two numbers together!")
    first = int(input("Please enter the first number: "))
    second = int(input("Please enter the second number: "))

    # process
    answer = first + second

    # output
    print("{} + {} = {}".format(first, second, answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
