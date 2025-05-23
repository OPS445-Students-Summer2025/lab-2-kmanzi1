#!/usr/bin/env python3

import sys

# Author: [Manzi Kevin
# Author ID: [Author ID: 183250232
# Date Created: 2025/05/23

# Checkiing if an argument is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <starting_number>")
    sys.exit(1)

# Assign a command-line argument to timer
try:
    timer = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

#thee  Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")