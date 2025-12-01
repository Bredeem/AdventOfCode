INPUT_FILE = "input.txt"


def part1(lines: list[str]):
    dial = 50
    hits = 0

    for line in lines:
        dir = line[0]
        num = int(line[1:])

        if dir == "R":
            dial = (dial + num) % 100
        else:
            dial = (dial - num) % 100

        if dial == 0:
            hits += 1

    print(f"Part 1: Code is {hits}")


def part2(lines: list[str]):
    dial = 50
    hits = 0

    for line in lines:
        dir = line[0]
        num = int(line[1:])

        if dir == "R":
            for _ in range(num):

                dial = (dial + 1) % 100
                if dial == 0:
                    hits += 1
        else:
            for _ in range(num):

                dial = (dial - 1) % 100
                if dial == 0:
                    hits += 1

    print(f"Part 2: Code is {hits}")


def main():

    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    lines = input_string.splitlines()
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
