import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

ranges = []
merged_ranges = []
fresh = set()
total_fresh = 0

with open(args.input) as f:
    parse_ranges = True

    for line in f:
        if line == '\n':
            parse_ranges = False
            for begin, end in sorted(ranges):
                if merged_ranges and merged_ranges[-1][1] >= begin - 1:
                    merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
                else:
                    merged_ranges.append([begin, end])

            for begin, end in merged_ranges:
                total_fresh += end - begin + 1
            continue

        if parse_ranges:
            begin, end = [int(x) for x in line.split('-')]
            ranges.append((begin, end))
        else:
            ingredientID = int(line)
            for begin, end in merged_ranges:
                if ingredientID < begin:
                    break
                if ingredientID <= end:
                    fresh.add(ingredientID)
                    break

print("part 1 fresh ingredients is " + str(len(fresh)))
print("part 2 fresh ingredients is " + str(total_fresh))
