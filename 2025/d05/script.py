INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def part1(id_ranges: list[tuple[int, int]], ids: list[int]):
    fresh_ids = 0
    for id in ids:
        for start, end in id_ranges:
            if start <= id <= end:
                fresh_ids += 1
                break

    print(f"Part 1: {fresh_ids}")


def find_overlap(a_s, a_e, b_s, b_e):
    s = max(a_s, b_s)
    e = min(a_e, b_e)
    if s > e:
        return 0
    return e - s + 1


def part2(id_ranges: list[tuple[int, int]]):
    fresh_ids = 0
    id_ranges.sort(key=lambda x: x[0])

    merged = []
    for start, end in id_ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    for start, end in merged:
        fresh_ids += end - start + 1

    print(f"Part 2: {fresh_ids}")


def main():

    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    id_ranges, ids = input_string.split("\n\n")
    id_ranges = [
        (int(r.split("-")[0]), int(r.split("-")[1])) for r in id_ranges.splitlines()
    ]
    ids = [int(id) for id in ids.splitlines()]

    part1(id_ranges, ids)
    part2(id_ranges)


if __name__ == "__main__":
    main()

