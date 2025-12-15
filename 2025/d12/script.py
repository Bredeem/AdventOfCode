from pprint import pprint

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def part1(shapes, regions):
    n = 0
    for size, boxes in regions:
        area = size[0] * size[1]

        if area >= sum(boxes) * 9:
            n += 1
        else:
            box_sum = sum(
                [
                    sum(
                        sum(map(sum, zip(*shapes[i]))) * n_box
                        for i, n_box in enumerate(boxes)
                    )
                ]
            )
            print(box_sum)
            if box_sum > area:
                continue
            else:
                print("somethings wrong!")

    print(f"Part 1: {n}")


def part2():

    print(f"Part 2: ")


def main():
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    shapes = input_string.split("\n\n")[:-1]
    regions = input_string.split("\n\n")[-1].splitlines()

    gift_shapes = []
    for shape in shapes:
        gift_shape = []
        for line in shape.splitlines()[1:]:
            gift_shape.append([1 if e == "#" else 0 for e in line])
        gift_shapes.append(gift_shape)

    tree_regions = []
    for region in regions:
        size, indecies = region.split(":")
        size = (int(size.split("x")[0]), int(size.split("x")[1]))
        indecies = [int(i) for i in indecies.strip().split(" ")]
        tree_regions.append((size, indecies))

    # pprint(gift_shapes)
    # print()
    # pprint(tree_regions)

    part1(gift_shapes, tree_regions)
    # part2()


if __name__ == "__main__":
    main()
