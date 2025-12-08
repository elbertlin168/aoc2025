import argparse
import networkx as nx

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

boxes = []
with open(args.input) as f:
    for line in f:
        boxes.append([int(x) for x in line.split(',')])

pairs = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = sum([(boxes[j][x] - boxes[i][x]) ** 2 for x in range(3)])
        pairs.append((distance, i, j))
pairs.sort()

G = nx.Graph()
G.add_nodes_from(range(len(boxes)))
G.add_edges_from([(pair[1], pair[2]) for pair in pairs[:1000]])
sizes = [len(circuit) for circuit in nx.connected_components(G)]
sizes.sort(reverse=True)

print("part 1 sizes product is " + str(sizes[0] * sizes[1] * sizes[2]))

i = 1000
while not nx.is_connected(G):
    G.add_edge(pairs[i][1], pairs[i][2])
    i += 1

last_box_a = pairs[i - 1][1]
last_box_b = pairs[i - 1][2]
print("part 2 x-coord product is " + str(boxes[last_box_a][0] * boxes[last_box_b][0]))
