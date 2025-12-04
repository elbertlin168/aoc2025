import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

part1_pw = 0
part2_pw = 0
dial = 50

with open(args.input) as f:
    for line in f:
        prev_dial = dial
        distance = int(line[1:])
        if line.startswith('R'):
            dial += distance
        else:
            dial -= distance

        quotient, remainder = divmod(dial, 100)

        if remainder == 0:
            part1_pw += 1

        part2_pw += abs(quotient)
        if dial <= 0:
            if remainder == 0:
                part2_pw += 1
            if prev_dial == 0:
                part2_pw -= 1

        dial = remainder

print("part 1 password is " + str(part1_pw))
print("part 2 password is " + str(part2_pw))
