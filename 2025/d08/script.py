from itertools import combinations
from math import pow, sqrt

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"

N_CONNECTIONS = 1000
# N_CONNECTIONS = 10


def euclidian_distance(a: list[int], b: list[int]):
    if len(a) != 3 or len(b) != 3:
        print("Invalid arrays:", a, b)
        return 0

    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))


def part1(input: list[list[int]]):
    # print(len(input))

    distances = []
    for a, b in combinations(input, 2):
        dist = euclidian_distance(a, b)
        distances.append([(a, b), dist])
    distances.sort(key=lambda x: x[1])

    # print(*distances[:1000], sep="\n")
    # print(len(distances))

    connections = [[p] for p in input]
    for i, elem in enumerate(distances):
        a, b = elem[0]
        dist = elem[1]
        if i == N_CONNECTIONS:
            break

        a_conn = next((p for p in connections if a in p), None)
        b_conn = next((p for p in connections if b in p), None)

        if not a_conn or not b_conn:
            print("Something is wrong, I can feel it...")
            continue
        if a_conn == b_conn:
            # print("skipping...")
            continue

        a_idx = connections.index(a_conn)

        connections[a_idx].extend(b_conn)
        connections.remove(b_conn)

    connections.sort(key=lambda x: len(x))
    # print(*connections, sep="\n")
    # print(len(connections))

    res = len(connections[-1]) * len(connections[-2]) * len(connections[-3])

    print(f"Part 1: {res}")


def part2(input: list[list[int]]):
    distances = []
    res = 0
    for a, b in combinations(input, 2):
        dist = euclidian_distance(a, b)
        distances.append([(a, b), dist])
    distances.sort(key=lambda x: x[1])

    connections = [[p] for p in input]
    for (a, b), dist in distances:
        a_conn = next((p for p in connections if a in p), None)
        b_conn = next((p for p in connections if b in p), None)

        if not a_conn or not b_conn:
            print("Something is wrong, I can feel it...")
            continue
        if a_conn == b_conn:
            # print("skipping...")
            continue

        a_idx = connections.index(a_conn)

        connections[a_idx].extend(b_conn)
        connections.remove(b_conn)

        if len(connections[0]) == len(input):
            res = a[0] * b[0]
            break

    print(f"Part 2: {res}")


def main():
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()
    input = [[int(x) for x in l.split(",")] for l in input_string.splitlines()]

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
