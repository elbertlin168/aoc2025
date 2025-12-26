import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

presents = {}
regions = []

with open(args.input) as f:
    line = 'start'
    present_line = False
    current_present = -1
    while line:
        line = f.readline()
        if len(line.split()) == 1 and not present_line:
            present_line = True
            current_present = int(line[:-2])
            presents[current_present] = []
        elif present_line:
            if line == '\n':
                present_line = False
            else:
                presents[current_present].append([True if x == '#' else False for x in line.strip()])
        elif line:
            region_line = line.split()
            w, l = [int(x) for x in region_line[0][:-1].split('x')]
            regions.append(((w, l), [int(x) for x in region_line[1:]]))

areas = {}
for i, shape in presents.items():
    areas[i] = sum(map(sum, shape))

fit_regions = 0
for region in regions:
    w, l = region[0]
    total_area = 0
    for i, count in enumerate(region[1]):
        total_area += areas[i] * count
    if total_area > w * l:
        continue
    fit_regions += 1

print("part 1 regions is " + str(fit_regions))
