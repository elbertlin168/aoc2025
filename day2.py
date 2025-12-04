import argparse
from math import log10

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

invalid_sum = 0

with open(args.input) as f:
    ranges = f.readline()
    for rnge in ranges.split(','):
        dash = rnge.index('-')
        firstID = int(rnge[:dash])
        lastID = int(rnge[dash+1:])

        first_half = int(log10(firstID)) // 2
        start = max(10 ** first_half, firstID // 10 ** (first_half + 1))
        last_half = (int(log10(lastID)) + 1) // 2
        end = min(lastID // 10 ** last_half + 1, 10 ** last_half)

        for half in range(start, end):
            invalid = half + half * 10 ** (int(log10(half)) + 1)
            if invalid >= firstID and invalid <= lastID:
                invalid_sum += invalid

print("invalid sum is " + str(invalid_sum))
