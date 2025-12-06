import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

numbers = []
operands = []
part1_total = 0

with open(args.input) as f:
    for line in f:
        if line[0] == '+' or line[0] == '*':
            operands = line.strip().split()
        else:
            numbers.append([int(x) for x in line.split()])

for i in range(len(operands)):
    if operands[i] == '+':
        problem = 0
        for j in range(len(numbers)):
            problem += numbers[j][i]
    else:
        problem = 1
        for j in range(len(numbers)):
            problem *= numbers[j][i]

    part1_total += problem

print("part 1 total is " + str(part1_total))

worksheet = []
part2_total = 0
with open(args.input) as f:
    worksheet = f.readlines()

op_line = len(worksheet) - 1
prv = 0
for nxt in range(len(worksheet[0])):
    if worksheet[op_line][nxt] != ' ':
        if worksheet[op_line][prv] == '+':
            problem = 0
            for i in range(prv, nxt):
                number_str = ''.join([worksheet[j][i] for j in range(op_line)]).strip()
                if number_str:
                    problem += int(number_str)
        else:
            problem = 1
            for i in range(prv, nxt):
                number_str = ''.join([worksheet[j][i] for j in range(op_line)]).strip()
                if number_str:
                    problem *= int(number_str)

        part2_total += problem
        prv = nxt

print("part 2 total is " + str(part2_total))
