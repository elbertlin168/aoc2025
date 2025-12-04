import argparse
from heapq import heappush, heappop

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

pq = []
grid = []
adj = []
total_rolls = 0

def update_adj(x, y, init=False):
    update = 1 if init else -1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            adj[x+i][y+j] += update
            if not init and grid[x+i][y+j] == '@' and [x+i,y+j] not in pq:
                heappush(pq, [x+i,y+j])

with open(args.input) as f:
    lines = f.readlines()
    width = len(lines[0]) + 1
    height = len(lines) + 2

    grid.append(['.' for _ in range(width)])
    adj = [[0] * width for _ in range(height)]

    for i in range(1, height - 1):
        line = lines[i-1]
        padded_line = '.' + line[:-1] + '.'
        grid.append(list(padded_line))
        for j in range(1, width - 1):
            if line[j-1] == '@':
                update_adj(i, j, init=True)
                heappush(pq, [i, j])

    grid.append(['.' for _ in range(width)])

while pq:
    x, y = heappop(pq)
    if adj[x][y] < 4:
        total_rolls += 1
        grid[x][y] = '.'
        update_adj(x, y)

print("part 2 removable rolls is " + str(total_rolls))
