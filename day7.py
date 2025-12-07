import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

beams = set()
splits = 0
particles = []

with open(args.input) as f:
    for line in f:
        if not beams:
            first = line.index('S')
            beams.add(first)
            particles = [0] * len(line.strip())
            particles[first] += 1
        else:
            new_beams = set()
            for beam in beams:
                if line[beam] == '^':
                    splits += 1
                    if beam > 0:
                        particles[beam - 1] += particles[beam]
                        new_beams.add(beam - 1)
                    if beam < len(line.strip()) - 1:
                        particles[beam + 1] += particles[beam]
                        new_beams.add(beam + 1)
                    particles[beam] = 0
                else:
                    new_beams.add(beam)
            beams = new_beams

print("part 1 beams is " + str(splits))
print("part 2 timelines is " + str(sum(particles)))
