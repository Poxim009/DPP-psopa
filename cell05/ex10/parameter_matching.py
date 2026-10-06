#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    secret = sys.argv[1]
    answer = input("What was the parameter? ")
    if answer == secret:
        print("Good job!")
    else:
        print("Nope, sorry...")