import os

# Day 2 of Advent of Code 2025
#
# - Read CSV-like input where each line contains comma-separated ranges, e.g.:
#   "11-22,95-115,998-1012"
# - For each range "start-end", add every integer in that inclusive range to IDlist.
# - For each number in IDlist:
#     * If it has an even number of digits,
#     * Split it into two equal halves (a and b),
#     * If a - b == 0 (i.e. a == b), count it as invalid.

# Build a path to the input file that is next to this script
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "Input.csv")   # change to "Example.csv" for the sample

IDlist: list[int] = []

with open(input_path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # Each line is a comma-separated list of ranges like "11-22"
        ranges = line.split(",")

        for r in ranges:
            r = r.strip()
            if not r:
                continue

            start_str, end_str = r.split("-")
            start = int(start_str)
            end = int(end_str)

            # Add every integer in the inclusive range [start, end]
            for n in range(start, end + 1):
                IDlist.append(n)

invalidcount = 0

for num in IDlist:
    s = str(num)

    # Only consider numbers with an even number of digits
    if len(s) % 2 != 0:
        continue

    mid = len(s) // 2
    a = int(s[:mid])
    b = int(s[mid:])

    if a - b == 0:
        print(num)
        invalidcount += num

#print(IDlist)
print("Number of invalid IDs:", invalidcount)