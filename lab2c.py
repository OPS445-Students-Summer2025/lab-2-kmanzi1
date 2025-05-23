#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Error: Please provide both a name and an age.")
    sys.exit(1)


name = sys.argv[1]
age = sys.argv[2]

print(f"Hi {name}, you are {age} years old.")