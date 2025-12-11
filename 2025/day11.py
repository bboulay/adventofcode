from operator import le
from typing import Optional


INPUT_FILE = "2025/day11.txt"
EXAMPLE_DATA = [
    "aaa: you hhh",
    "you: bbb ccc",
    "bbb: ddd eee",
    "ccc: ddd eee fff",
    "ddd: ggg",
    "eee: out",
    "fff: out",
    "ggg: out",
    "hhh: ccc fff iii",
    "iii: out"
]
EXAMPLE_DATA_2 = [
    "svr: aaa bbb",
    "aaa: fft",
    "fft: ccc",
    "bbb: tty",
    "tty: ccc",
    "ccc: ddd eee",
    "ddd: hub",
    "hub: fff",
    "eee: dac",
    "dac: fff",
    "fff: ggg hhh",
    "ggg: out",
    "hhh: out",
]


def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


def parse_data(data: list[str]) -> dict[str, list[str]]:
    parsed = {}
    for line in data:
        temp = line.split(": ")
        parsed[temp[0]] = temp[1].split(" ")
    return parsed


def compute_paths(data: dict, start: str, end: str, path: Optional[list[str]] = None) -> list[list[str]]:
    """
    Recursively compute all paths from start to end in the graph.

    Args:
        data (dict): The graph represented as an adjacency list.
        start (str): The starting node.
        end (str): The ending node.
        path (list[str], optional): The current path being explored. Defaults to None.

    Returns:
        list[list[str]]: A list of all paths from start to end.
    """
    if path is None:
        path = []

    path = path + [start]  # Add the current node to the path

    if start == end:
        return [path]  # Return the completed path

    if start not in data:
        return []  # No paths if the start node has no neighbors

    paths = []
    for node in data[start]:
        if node not in path:  # Avoid cycles
            new_paths = compute_paths(data, node, end, path)
            paths.extend(new_paths)

    return paths


def compute_paths2(data: dict, start: str, end: str, cached_paths: dict[(str, str), int] = {}) -> int:
    if start == end:
        return 1
    
    if start == 'out':
        return 0
    
    if (start, end) in cached_paths:
        return cached_paths[(start, end)]

    paths = 0
    for node in data[start]:
        paths += compute_paths2(data, node, end, cached_paths)
    
    cached_paths[(start, end)] = paths
    return paths


def part1(data: dict) -> int:
    result = 0
    start = "you"
    end = "out"
    
    paths = compute_paths(data, start, end)
    #print(paths)
    result = len(paths)
    
    return result


def part2(data: dict) -> int:
    start = "svr"
    string1 = "fft"
    string2 = "dac"
    end = "out"
    
    result = compute_paths2(data, start, string1)
    result *= compute_paths2(data, string1, string2)
    result *= compute_paths2(data, string2, end)
    
    result2 = compute_paths2(data, start, string2)
    result2 *= compute_paths2(data, string2, string1)
    result2 *= compute_paths2(data, string1, end)
    
    return result + result2


if __name__ == "__main__":
    data = EXAMPLE_DATA  # For testing with example data
    data = read_data(INPUT_FILE)
    parsed_data = parse_data(data)
   #print(parsed_data)
    print("Part 1:", part1(parsed_data))
    data = EXAMPLE_DATA_2
    data = read_data(INPUT_FILE)
    parsed_data = parse_data(data)
    print("Part 2:", part2(parsed_data))