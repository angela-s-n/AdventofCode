import csv
import os

# Day 1 of Advent of Code 2025

start = 50
x = start          # current dial position, always kept in 0–99
password = 0       # how many times we touch 0

# Build a path to the input file that is next to this script
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "Input.csv")  # change to "Input.csv" for real run

with open(input_path) as f:
    for line in f:
        line = line.strip()     # remove newline/whitespace
        if not line:            # skip empty lines if any
            continue

        direction = line[0]     # 'L' or 'R'
        value = int(line[1:])   # rest of the line as an int

        # Move one step at a time and count every time we land on 0.
        for _ in range(value):
            if direction == "L":
                x = (x - 1) % 100
            elif direction == "R":
                x = (x + 1) % 100

            # Toggle on if want to count how many times 0 is clicked on
            #if x == 0:
                #password += 1
        if x == 0:
                password += 1

print("The final password is: ", password)
