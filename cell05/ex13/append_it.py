#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if not re.search(r"ism$", param):
            print(f"{param}ism")

# python append_it.py "parallel" "egoism" "human"