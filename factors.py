#!/usr/bin/python3

import sys
import time


def factorize(n):
    """
    Attempt to factorize the number into two smaller numbers.
    """
    root = int(n ** .5) + 1
    for i in range(2, root):
        if n % i == 0:
            return i, n // i
    return n, 1


try:
    """
    handle reading of files and numbers
    """
    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            try:
                num = int(line)
                p, q = factorize(num)
                print(f"{num}={p}*{q}")
            except ValueError:
                print(f"Skipping invalid line: {line}")

except FileNotFoundError:
    print(f"{sys.argv[1]} not found")

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)
