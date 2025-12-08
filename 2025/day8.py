from typing import Tuple
from math import sqrt

INPUT_FILE = "day8.txt"
EXAMPLE_DATA = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]


def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def parse_data(data: list[str]) -> list[list[int]]:
    positions = []
    for line in data:
        positions.append([int(item) for item in line.split(",")])
    return positions


def euclidean_distance(point1: list[int], point2: list[int]) -> float | None:
    distance = 0
    if len(point1) != len(point2):
        return None
    for index, value in enumerate(point1):
        distance += (value - point2[index]) ** 2

    return sqrt(distance)


def are_already_connected(
    index1: int, index2: int, connections: list[set[int]]
) -> bool:
    for connection in connections:
        if index1 in connection and index2 in connection:
            return True
    return False


def closest_points(
    points: list[list[int]], distances: dict, connections: list[set[int]]
) -> Tuple[int, int]:
    index_point_1 = 0
    index_point_2 = 1
    min_distance = euclidean_distance(points[0], points[1])

    for index1, point1 in enumerate(points):
        for index2, point2 in enumerate(points):
            if index1 <= index2:
                continue
            temp_distance = distances[index1][index2]
            if temp_distance < min_distance:
                if are_already_connected(index1, index2, connections):
                    continue
                min_distance = temp_distance
                index_point_1 = index1
                index_point_2 = index2

    return index_point_1, index_point_2


def compute_all_distances(points: list[list[int]]) -> dict:
    distances = {}
    for index1, point1 in enumerate(points):
        for index2, point2 in enumerate(points):
            if index1 <= index2:
                continue
            temp_distance = euclidean_distance(point1, point2)
            distances[(index1, index2)] = temp_distance

    return distances


def part1(positions: list[list[int]], number_pair: int = 10) -> int:
    print(positions)
    connections: list[set] = []
    distances = compute_all_distances(positions)
    # sort the distance
    distances = sorted(distances.items(), key=lambda x: x[1])

    for (i, j), d in distances[:number_pair]:
        _id_i = -1
        _id_j = -1

        for idx, s in enumerate(connections):
            if i in s:
                _id_i = idx
            if j in s:
                _id_j = idx

        match (_id_i > -1, _id_j > -1):
            case (False, False):
                connections.append({i, j})
            case (True, False):
                connections[_id_i].add(j)
            case (False, True):
                connections[_id_j].add(i)
            case (True, True) if _id_i != _id_j:
                connections[_id_i] |= connections[_id_j]
                del connections[_id_j]

    connections = sorted(connections, key=len, reverse=True)

    return len(connections[0]) * len(connections[1]) * len(connections[2])


def part2(positions: list[list[int]]) -> int:
    print(positions)
    connections: list[set] = []
    connected = set()
    distances = compute_all_distances(positions)
    # sort the distance
    distances = sorted(distances.items(), key=lambda x: x[1])

    print(distances)

    for (i, j), d in distances:
        _id_i = -1
        _id_j = -1

        connected.add(i)
        connected.add(j)

        for idx, s in enumerate(connections):
            if i in s:
                _id_i = idx
            if j in s:
                _id_j = idx

        match (_id_i > -1, _id_j > -1):
            case (False, False):
                connections.append({i, j})
            case (True, False):
                connections[_id_i].add(j)
            case (False, True):
                connections[_id_j].add(i)
            case (True, True) if _id_i != _id_j:
                connections[_id_i] |= connections[_id_j]
                del connections[_id_j]
        # print(len(connected), len(positions), len(connections))
        if len(connected) == len(positions) and len(connections) == 1:
            return positions[i][0] * positions[j][0]

    return -1


if __name__ == "__main__":
    data = EXAMPLE_DATA
    data = read_data(INPUT_FILE)
    grid = parse_data(data)
    result_part1 = part1(grid, 1000)
    print("Part 1: ", result_part1)
    result_part2 = part2(grid)
    print("Part 2: ", result_part2)
