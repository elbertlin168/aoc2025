import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

total_rolls = 0

def accessible_rolls(line_above, line, line_below):
    rolls = 0
    count_above = line_above[:3].count('@')
    count_lr = line[:3:2].count('@')
    count_below = line_below[:3].count('@')

    for i in range(1, len(line) - 1):
        if line[i] == '@':
            if count_above + count_lr + count_below < 4:
                rolls += 1

        if i == len(line) - 2:
            break
        
        if line_above[i-1] == '@':
            count_above -= 1
        if line_above[i+2] == '@':
            count_above += 1

        count_lr = line[i:i+3:2].count('@')

        if line_below[i-1] == '@':
            count_below -= 1
        if line_below[i+2] == '@':
            count_below += 1

    return rolls

def pad_line(line):
    return '.' + line + '.'

with open(args.input) as f:
    line_b = f.readline()
    line_a = '.' * (len(line_b) - 1) + '\n'
    line_c = f.readline()

    while line_c:
        total_rolls += accessible_rolls(pad_line(line_a[:-1]), pad_line(line_b[:-1]), pad_line(line_c[:-1]))
        line_a = line_b
        line_b = line_c
        line_c = f.readline()

    line_c = '.' * (len(line_b) - 1) + '\n'
    total_rolls += accessible_rolls(pad_line(line_a[:-1]), pad_line(line_b[:-1]), pad_line(line_c[:-1]))

print("part 1 accessible rolls is " + str(total_rolls))
