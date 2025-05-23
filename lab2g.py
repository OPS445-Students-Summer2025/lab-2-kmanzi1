#!/usr/bin/env python3

import sys

# Author: Manzi Kevin
# Author ID:  183250232
# Date Created: 2025/05/23

# Determine the timer value based on command-line argument
if len(sys.argv) == 2:
    try:
        timer = int(sys.argv[1])  # Convert argument to integer
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)
else:
    timer = 3  # Default value if no argument is given

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")