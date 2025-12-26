import argparse
from collections import deque
from pulp import LpProblem, lpSum, LpVariable, PULP_CBC_CMD

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def configure_lights(curr, goal, buttons):
    if curr == goal:
        return 0

    queue = deque([(curr, button, 0) for button in buttons])

    while queue:
        prv, button, presses = queue.popleft()
        nxt = list(prv)
        for light in button:
            nxt[light] = '#' if prv[light] == '.' else '.'
        nxt = ''.join(nxt)
        if nxt == goal:
            return presses + 1
        queue.extend([(nxt, button, presses + 1) for button in buttons])

def configure_joltage(goal, buttons):
    model = LpProblem()

    variables = []
    for i, button in enumerate(buttons):
        variables.append(LpVariable(name='Button' + str(i), lowBound=0, cat='Integer'))

    model += lpSum(variables)

    for j, joltage in enumerate(goal):
        model += (
            lpSum([variables[i] for i in range(len(buttons)) if j in buttons[i]]) == joltage,
            'Joltage' + str(j)
        )

    model.solve(PULP_CBC_CMD(msg=False))

    return int(model.objective.value())

p1_presses = 0
p2_presses = 0

with open(args.input) as f:
    for line in f:
        split = line.split()

        lights = '.' * (len(split[0]) - 2)
        buttons = []
        for button in split[1:-1]:
            buttons.append(tuple([int(x) for x in button[1:-1].split(',')]))
        goal_joltage = [int(x) for x in split[-1][1:-1].split(',')]

        p1_presses += configure_lights(lights, split[0][1:-1], buttons)
        p2_presses += configure_joltage(goal_joltage, buttons)

print("part 1 total presses is " + str(p1_presses))
print("part 2 total presses is " + str(p2_presses))
