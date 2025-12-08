INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def part1(input: list[str]):
    total = 0
    equation = []
    for i in range(len(input[0])):
        bp = True
        for j in range(len(input)):
            if not (0 <= j < len(equation)):
                equation.append(input[j][i])
                bp = False
            else:
                if not (input[j][i] == " " or input[j][i] == "\n"):
                    bp = False
                equation[j] += input[j][i]

        if bp:
            # print("summing eq:", equation)
            sum = 0
            if equation[-1].strip() == "+":
                for n in equation[:-1]:
                    sum += int(n.strip())
            else:
                for n in equation[:-1]:
                    if sum == 0:
                        sum = int(n.strip())
                    else:
                        sum *= int(n.strip())
            # print("sum:", sum)
            total += sum
            equation = []

    print(f"Part 1: {total}")


def part2(input: list[str]):
    total = 0
    equation = []
    for i in range(len(input[0]) - 1, -1, -1):
        equation.append("")
        for j in range(len(input) - 1):
            equation[-1] += input[j][i]

        op = input[-1][i]
        if op == "+" or op == "*":
            # print("summing eq:", equation)
            # print("op:", op)
            sum = 0
            if op == "+":
                for n in equation:
                    if n.strip() == "":
                        continue
                    sum += int(n.strip())
            else:
                for n in equation:
                    if n.strip() == "":
                        continue
                    if sum == 0:
                        sum = int(n.strip())
                    else:
                        sum *= int(n.strip())
            # print("sum:", sum)
            total += sum
            equation = []

    print(f"Part 2: {total}")


def main():

    with open(INPUT_FILE, "r") as f:
        input_strings = f.readlines()

        part1(input_strings)
        part2(input_strings)


if __name__ == "__main__":
    main()

