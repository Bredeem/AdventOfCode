import re

INPUT_FILE = "input.txt"

def swap(idx_a, idx_b, li):
    tmp = li[idx_a]
    li[idx_a] = li[idx_b]
    li[idx_b] = tmp


def part1(disk_string: str):

    reformated_disk = []

    block_id = 0
    for i, c in enumerate(disk_string):
        if i % 2 == 0:
            reformated_disk += ([str(block_id)] * int(c))
            block_id += 1
        else:
            if not c == "0":
                reformated_disk += (["."] * int(c))
    
    num_digits = len([d for d in reformated_disk if d != "."])
    # print(reformated_disk)
    # print("".join(reformated_disk))


    last_digit_idx = len(reformated_disk)-1
    for i, c in enumerate(reformated_disk):
        
        while reformated_disk[last_digit_idx] == ".":
            last_digit_idx -= 1

        if c == ".":
            if i >= num_digits:
                break
            
            swap(i, last_digit_idx, reformated_disk)
            # print("".join(reformated_disk))

            
    checksum = 0
    for i, c in enumerate(reformated_disk):
        if c != ".":
            checksum += (i * int(c))

    print(f"Part 1: {checksum}")


def find_available_space(disk, size):
    start = -1
    for i, block in enumerate(disk):
        if start == -1: 
            if block == ".":
                start = i
        else:
            if block != ".":
                if i - start >= size:
                    return start
                start = -1
    return -1

def part2(disk_string: str):
    reformated_disk = []

    block_id = 0
    for i, c in enumerate(disk_string):
        if i % 2 == 0:
            reformated_disk += ([str(block_id)] * int(c))
            block_id += 1
        else:
            if not c == "0":
                reformated_disk += (["."] * int(c))


    # print(reformated_disk)
    for id in range(block_id-1, 0, -1):
        string = "".join(reformated_disk)
        
        file_size = reformated_disk.count(str(id))
        file_idx = reformated_disk.index(str(id))

        # print(f"{id=}, {file_size=}")
        # print(string)
        free_space_idx = find_available_space(reformated_disk, file_size)


        if free_space_idx != -1:
            # print(f"start={free_space_idx}")
            if free_space_idx < file_idx:
                for i in range(file_size):
                    swap(free_space_idx + i, file_idx + i, reformated_disk)

                # print("".join(reformated_disk))

    checksum = 0
    # print("".join(reformated_disk))

    for i, c in enumerate(reformated_disk):
        if c != ".":
            checksum += (i * int(c))
    
    print(f"Part 2: {checksum}")


def main():
    
    with open(INPUT_FILE, "r") as f:
        input_string = f.read().strip()


    part1(input_string)
    part2(input_string)

if __name__ == '__main__':
    main()