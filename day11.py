import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

devices = {}
reverse = {}
distances = {}

with open(args.input) as f:
    for line in f:
        split = line.strip().split()
        devices[split[0][:-1]] = split[1:]
        for d in split[1:]:
            if d not in reverse:
                reverse[d] = []
            reverse[d].append(split[0][:-1])

def get_paths_to_out(device):
    if devices[device][0] == 'out':
        return 1

    paths = 0
    for d in devices[device]:
        paths += get_paths_to_out(d)
    return paths

print("part 1 paths is " + str(get_paths_to_out('you')))

def get_distance_to_out(device):
    if device not in distances:
        if devices[device][0] == 'out':
            distances[device] = 1
        else:
            distance = 0
            for d in devices[device]:
                distance = max(distance, get_distance_to_out(d) + 1)
            distances[device] = distance
    return distances[device]

for device in devices:
    get_distance_to_out(device)

def get_paths(start, end, distances, halfway=0, on_path=None):
    if distances[start] <= distances[end]:
        return 0
    if end in devices[start]:
        return 1

    paths = 0
    if not on_path and distances[start] - distances[end] > 10:
        halfway = (distances[start] + distances[end]) / 2
        on_path = {end}
        to_check = [end]
        while to_check:
            dest = to_check.pop()
            for d in reverse[dest]:
                if distances[d] <= halfway:
                    on_path.add(d)
                    to_check.append(d)

    for d in devices[start]:
        if distances[d] > halfway or d in on_path:
            paths += get_paths(d, end, distances, halfway, on_path)
    return paths

if distances['fft'] > distances['dac']:
    path_0 = get_paths('svr', 'fft', distances)
    path_1 = get_paths('fft', 'dac', distances)
    path_2 = get_paths_to_out('dac')
else:
    path_1 = get_paths('svr', 'dac', distances)
    path_1 = get_paths('dac', 'fft', distances)
    path_2 = get_paths_to_out('fft')

print("part 2 paths is " + str(path_0 * path_1 * path_2))
