INPUT_FILE = "day7.txt"
EXAMPLE_DATA = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "..............."
]

def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def parse_data(data: list[str]) -> list[list[str]]:
    entries = []
    for line in data:
        entries.append(list(line))
    return entries

def part1(grid: list[list[str]]) -> int:
    number_rows = len(grid)
    number_columns = len(grid[0])
    list_beams = set()
    for index, value in enumerate(grid[0]):
        if value == "S":
            list_beams.add(index)
            break

    number_split = 0
    for row in grid[1:]:
        new_beams = set()
        for index in list_beams:
            if row[index] == ".":
                new_beams.add(index)
            elif row[index] == "^":
                number_split += 1
                if index - 1 >= 0:
                    new_beams.add(index - 1)
                if index + 1 < number_columns:
                    new_beams.add(index + 1)
        #print(new_beams)
        list_beams = new_beams

    return number_split

def part2(grid: list[list[str]]) -> int:
    number_rows = len(grid)
    number_columns = len(grid[0])
    paths = dict()
    for index, value in enumerate(grid[0]):
        if value == "S":
            paths[index] = 1
            break

    number_timeline = 0
    for i, row in enumerate(grid[1:]):
        new_paths = dict()
        for path in paths.keys():
            if row[path] == ".":
                if path not in new_paths:
                    new_paths[path] = 0
                new_paths[path] += paths[path]
            elif row[path] == "^":
                if path - 1 >= 0:
                    if path - 1 not in new_paths:
                        new_paths[path - 1] = 0
                    new_paths[path - 1] += paths[path]
                else:
                    number_timeline += paths[path]
                if path + 1 < number_columns:
                    if path + 1 not in new_paths:
                        new_paths[path + 1] = 0
                    new_paths[path +1 ] += paths[path]
                else:
                    number_timeline += paths[path]
        paths = new_paths.copy()

        #print(i, paths, number_timeline)

    for nb_t in paths.values():
        number_timeline += nb_t

    return number_timeline

if __name__ == "__main__":
    data = EXAMPLE_DATA
    data = read_data(INPUT_FILE)
    grid = parse_data(data)
    result_part1 = part1(grid)
    print("Part 1: ", result_part1)
    result_part2 = part2(grid)
    print("Part 2: ", result_part2)
