import argparse
from math import log10, ceil

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

part1_sum = 0
part2_sum = 0

with open(args.input) as f:
    ranges = f.readline()
    for rnge in ranges.split(','):
        dash = rnge.index('-')
        firstID = int(rnge[:dash])
        lastID = int(rnge[dash+1:])

        first_digits = int(log10(firstID)) + 1
        last_digits = int(log10(lastID)) + 1

        invalid_set = set()
        for repeat in range(2, last_digits + 1):
            first_slice = ceil(first_digits / repeat)
            start = max(10 ** (first_slice - 1), firstID // 10 ** ((repeat - 1) * first_slice))
            last_slice = last_digits // repeat
            end = min(lastID // 10 ** last_slice + 1, 10 ** last_slice)

            for slce in range(start, end):
                invalid = 0
                slce_digits = int(log10(slce)) + 1
                for i in range(repeat):
                    invalid += slce * 10 ** (i * slce_digits)

                if invalid >= firstID and invalid <= lastID:
                    invalid_set.add(invalid)
                    if repeat == 2:
                        part1_sum += invalid

        part2_sum += sum(invalid_set)

print("part 1 invalid sum is " + str(part1_sum))
print("part 2 invalid sum is " + str(part2_sum))
