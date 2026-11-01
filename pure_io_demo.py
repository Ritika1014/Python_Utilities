#!/usr/bin/env python3
import sys

# INPUT: Read from stdin
print("Enter your name:")
name = sys.stdin.readline().strip()
print(f"Read from stdin: {name}")

# OUTPUT: Write to stdout
sys.stdout.write("Hello from stdout!\n")
sys.stdout.write(f"Name: {name}\n")

# ERROR: Only show stderr when there's an actual error
try:
    # Try to convert input to integer (this might fail)
    age = int(input("Enter your age: "))
    print(f"Age: {age}")
except ValueError:
    sys.stderr.write("Error: Please enter a valid number for age\n")
    sys.stderr.flush()

print("Pure I/O demonstration complete!")
