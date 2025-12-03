# INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"


def part1(banks: list[str]):
    total_joltage = 0

    for bank in banks:
        a = max(bank[: len(bank) - 1])
        b = max(bank[bank.index(a) + 1 :])
        total_joltage += int(a + b)
        # print(a + b)

    print(f"Part 1: Total joltage is {total_joltage}")


def part2(banks: list[str]):
    total_joltage = 0

    for bank in banks:
        slice = bank
        joltage = ""
        for n in range(11, -1, -1):
            n = max(slice[: len(slice) - n])
            slice = slice[slice.index(n) + 1 :]
            # print(slice)
            # print(n)
            joltage += n

        total_joltage += int(joltage)
        # print(joltage)

    print(f"Part 2: Total joltage is {total_joltage}")


def main():

    with open(INPUT_FILE, "r") as f:
        input = f.read().splitlines()
        part1(input)
        part2(input)


if __name__ == "__main__":
    main()
