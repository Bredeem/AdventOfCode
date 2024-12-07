from itertools import product
import re

INPUT_FILE = "input.txt"


def part2(calibrations: list[str]):
    sum = 0

    for calibration in calibrations:
        ans, nums = calibration.strip().split(":")

        ans = int(ans)
        nums = [int(n) for n in nums.strip().split(" ")]

         # print(f"{nums=}")
        for ops in product(["add", "mul", "cat"], repeat=len(nums)-1):
            # print(f"{ops=}")
            res = nums[0]
            for i, op in enumerate(ops, start=1):
                if res > ans:
                    break
                if op == "add":
                    res += nums[i]
                elif op == "mul":
                    res *= nums[i]
                elif op == "cat":
                    res = int(str(res) +str(nums[i]))
            # print(f"{test_ans=}")

            if res == ans:
                # print(ans, nums, ops)
                sum += res
                break

   
    print(f"Part 2: {sum}")


def part1(calibrations: list[str]):
    
    sum = 0

    for calibration in calibrations:
        ans, nums = calibration.strip().split(":")

        ans = int(ans)
        nums = [int(n) for n in nums.strip().split(" ")]

        # print(f"{nums=}")
        for ops in product(["add", "mul"], repeat=len(nums)-1):
            # print(f"{ops=}")
            res = nums[0]
            for i, op in enumerate(ops, start=1):
                if op == "add":
                    res += nums[i]
                elif op == "mul":
                    res *= nums[i]
            
            # print(f"{test_ans=}")

            if res == ans:
                # print(ans, nums, ops)
                sum += res
                break
    
    print(f"Part 1: {sum}")


def main():
    
    with open(INPUT_FILE, "r") as f:
        input_li = f.readlines()
    
    part1(input_li)
    part2(input_li)


if __name__ == '__main__':
    main()