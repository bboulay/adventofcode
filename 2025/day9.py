from typing import Tuple


INPUT_FILE = "2025/day9.txt"
EXAMPLE_DATA = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]


def read_data(file_path: str) -> list[str]:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        list[str]: _description_
    """
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


def parse_data(data: list[str]) -> list[Tuple[int, int]]:
    """_summary_

    Args:
        data (list[str]): _description_

    Returns:
        list[Tuple[int, int]]: _description_
    """
    positions = []
    for line in data:
        x, y = line.split(",")
        positions.append((int(x), int(y)))
    return positions


def compute_all_areas(positions: list[Tuple[int, int]]) -> dict[Tuple[int, int], int]:
    areas = {}
    for i, point1 in enumerate(positions):
        for j, point2 in enumerate(positions):
            if i >= j:
                continue
            area = compute_area(point1, point2)
            areas[(i, j)] = area
    return areas


def compute_all_areas_with_green_tiles(
    positions: list[Tuple[int, int]], perimeter: list[Tuple[int, int]]
) -> dict[Tuple[int, int], int]:
    areas = {(-1, 1): -1}
    for i, point1 in enumerate(positions):
        for j, point2 in enumerate(positions):
            if i >= j:
                continue
            area = compute_area(point1, point2)
            if area <= max(areas.values()):
                continue
            if not is_valid_rectangle(point1, point2, perimeter):
                # print(i, j)
                # print("invalid rectangle")
                continue

            areas[(i, j)] = area
    return areas


def compute_area(pair1: Tuple[int, int], pair2: Tuple[int, int]) -> int:
    """_summary_

    Args:
        pair1 (Tuple[int, int]): _description_
        pair2 (Tuple[int, int]): _description_

    Returns:
        int: _description_
    """
    area = abs(abs(pair1[0] - pair2[0]) + 1) * (abs(pair1[1] - pair2[1]) + 1)

    return area


def construct_perimeter(positions: list[Tuple[int, int]]) -> list:
    perimeter = [
        (min(c1, c2), max(c1, c2))
        for c1, c2 in zip(positions, positions[1:] + positions[:1])
    ]
    return perimeter


def is_valid_rectangle(
    point1: Tuple[int, int], point2: Tuple[int, int], perimeter: list
):
    x1, x2 = sorted([point1[0], point2[0]])
    y1, y2 = sorted([point1[1], point2[1]])

    if any(
        edge_x2 > x1 and edge_x < x2 and edge_y2 > y1 and edge_y < y2
        for (edge_x, edge_y), (edge_x2, edge_y2) in perimeter
    ):
        # A "green line" intersects the rectangle, this rectangle is invalid
        return False

    return True


def part1(data: list[Tuple[int, int]]) -> int:
    """_summary_

    Args:i
        positions (list[Tuple[int, int]]): _description_

    Returns:
        int: _description_
    """
    areas = compute_all_areas(data)
    areas = sorted(areas.items(), key=lambda x: x[1])
    # print(areas)
    # print(data[areas[-1][0][0]], data[areas[-1][0][1]], areas[-1][1])
    return areas[-1][1]


def part2(positions: list[Tuple[int, int]]) -> int:
    """_summary_

    Args:
        positions (list[Tuple[int, int]]): _description_

    Returns:
        int: _description_
    """
    perimeter = construct_perimeter(positions)
    #print(perimeter)
    areas = compute_all_areas_with_green_tiles(positions, perimeter)
    areas = sorted(areas.items(), key=lambda x: x[1])
    #print(areas)
    #print(positions[areas[-1][0][0]], positions[areas[-1][0][1]], areas[-1][1])
    return areas[-1][1]


if __name__ == "__main__":
    data = EXAMPLE_DATA
    data = read_data(INPUT_FILE)
    data = parse_data(data)
    result_part1 = part1(data)
    print(f"Part 1: {result_part1}")
    result_part2 = part2(data)
    print(f"Part 2: {result_part2}")
