import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

part1_joltage = 0
part2_joltage = 0

with open(args.input) as f:
    for line in f:
        max_ten = max(line[:-2])
        max_ten_idx = line.index(max_ten)
        max_one = max(line[max_ten_idx+1:])
        part1_joltage += int(max_ten + max_one)

        joltage = ''
        start = 0
        for i in range(12):
            max_digit = max(line[start:-12+i])
            start += line[start:].index(max_digit) + 1
            joltage += max_digit
        part2_joltage += int(joltage)

print("part 1 total joltage is " + str(part1_joltage))
print("part 2 total joltage is " + str(part2_joltage))
