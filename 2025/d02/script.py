import re

# INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"


def part1(ranges: list[tuple[int, int]]):
    sum = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            length = len(str(n))
            if length % 2 != 0:
                continue
            if str(n)[: int(length / 2)] == str(n)[int(length / 2) :]:
                # print(n)
                sum += n

    print(f"Part 1: Sum is {sum}")


def part2(ranges: list[tuple[int, int]]):
    sum = 0

    pattern = re.compile(r"^(\d+)(\1)+$")

    for start, end in ranges:
        for n in range(start, end + 1):
            if pattern.match(str(n)):
                # print(n)
                sum += n

    print(f"Part 2: Sum is {sum}")


def main():

    with open(INPUT_FILE, "r") as f:
        input_string = f.read()
        ranges = [
            (int(r.split("-")[0]), int(r.split("-")[1]))
            for r in input_string.split(",")
        ]
        part1(ranges)
        part2(ranges)


if __name__ == "__main__":
    main()
