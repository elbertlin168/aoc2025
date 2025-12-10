import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

tiles = []
edges_h = []
edges_v = []
areas = {}
max_area = 0

with open(args.input) as f:
    prv = None
    for line in f:
        x, y = [int(i) for i in line.split(',')]
        for tile in tiles:
            area = (abs(tile[0] - x) + 1) * (abs(tile[1] - y) + 1)
            areas[frozenset({(x, y), (tile[0], tile[1])})] = area
            max_area = max(max_area, area)
        if prv:
            edges = edges_v if x == prv[0] else edges_h
            edges.append((prv, (x, y)))
        tiles.append((x, y))
        prv = (x, y)
    edges = edges_v if prv[0] == tiles[0][0] else edges_h
    edges.append((prv, tiles[0]))

print("part 1 max area is " + str(max_area))

def is_valid(tile_a, tile_b, edges_h, edges_v):
    rect_r = max(tile_a[0], tile_b[0])
    rect_l = min(tile_a[0], tile_b[0])
    rect_t = max(tile_a[1], tile_b[1])
    rect_b = min(tile_a[1], tile_b[1])
    for edge in edges_h:
        if edge[0][1] < rect_b or edge[0][1] > rect_t:
            continue
        if edge[1][0] > edge[0][0]:
            if edge[0][1] != rect_b:
                if edge[0][0] < rect_r and edge[1][0] >= rect_r:
                    return False
                if edge[0][0] <= rect_l and edge[1][0] > rect_l:
                    return False
        else:
            if edge[0][1] != rect_t:
                if edge[0][0] >= rect_r and edge[1][0] < rect_r:
                    return False
                if edge[0][0] > rect_l and edge[1][0] <= rect_l:
                    return False
    for edge in edges_v:
        if edge[0][0] < rect_l or edge[0][0] > rect_r:
            continue
        if edge[1][1] > edge[0][1]:
            if edge[0][0] != rect_r:
                if edge[0][1] < rect_t and edge[1][1] >= rect_t:
                    return False
                if edge[0][1] <= rect_b and edge[1][1] > rect_b:
                    return False
        else:
            if edge[0][0] != rect_l:
                if edge[0][1] >= rect_t and edge[1][1] < rect_t:
                    return False
                if edge[0][1] > rect_b and edge[1][1] <= rect_b:
                    return False
    return True

max_area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        if is_valid(tiles[i], tiles[j], edges_h, edges_v):
            max_area = max(max_area, areas[frozenset({tiles[i], tiles[j]})])

print("part 2 max area is " + str(max_area))
