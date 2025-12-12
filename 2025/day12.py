INPUT_FILE = "2025/day12.txt"
EXAMPLE_DATA = [
    "0:",
    "###",
    "##.",
    "##.",
    "",
    "1:",
    "###",
    "##.",
    ".##",
    "",
    "2:",
    ".##",
    "###",
    "##.",
    "",
    "3:",
    "##.",
    "###",
    "##.",
    "",
    "4:",
    "###",
    "#..",
    "###",
    "",
    "5:",
    "###",
    ".#.",
    "###",
    "",
    "4x4: 0 0 0 0 2 0",
    "12x5: 1 0 1 0 2 2",
    "12x5: 1 0 1 0 3 2",
]


def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


def parse_data(data: list[str]) -> tuple[dict[int, tuple[int, list[str]]], list[tuple[int, int, list[int]]]]:
    shapes = {}
    regions = []
    current_shape = []
    shape_id = None
    shape_area = 0
    for line in data:
        if 'x' in line:
            # This is a region
            temp = line.split(": ")
            dimensions = temp[0].split('x')
            width = int(dimensions[0])
            height = int(dimensions[1])
            shape_ids = list(map(int, temp[1].split(" ")))
            regions.append((width, height, shape_ids))
            continue
        if ':' in line:
            # This is a new shape
            shape_id = int(line[:-1])
            current_shape = []
            continue
        if line == "":
            # this end the current shape
            shapes[shape_id] = (shape_area, current_shape)
            current_shape = []
            shape_id = None
            shape_area = 0
            continue
        current_shape.append(line)
        shape_area += line.count('#')
    return shapes, regions


def part1(shapes: dict[int, tuple[int, list[str]]], regions: list[tuple[int, int, list[int]]]) -> int:
    result = 0
    for width, height, number_shape_ids in regions:
        region_area = width * height
        desired_area = 0
        for index, number_shape_id in enumerate(number_shape_ids):
            shape_area, _ = shapes[index]
            desired_area += number_shape_id * shape_area

        if desired_area * 1.2 < region_area:
                result += 1      
           
    return result


if __name__ == "__main__":
    data = EXAMPLE_DATA
    data = read_data(INPUT_FILE)
    shapes, regions = parse_data(data)
    print(shapes, regions)
    print("Part 1:", part1(shapes, regions))

