INPUT_FILE = "day4.txt"
EXEMPLE_DATA = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

ROWS = [-1, 0, 1]
COLUMNS = [-1, 0, 1]

def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def parse_data(data: list[str]) -> list[list[int]]:
    rolls = []
    for line in data:
        roll = [1 if char == "@" else 0 for char in line]
        rolls.append(roll)
    return rolls

def get_value(rolls: list[list[int]], row, column) -> int:
    number_row = len(rolls)
    number_column = len(rolls[0])
    if row >= number_row or column >= number_column or row < 0 or column < 0:
        return 0
    return rolls[row][column]

def is_valid_roll(rolls: list[list[int]], row, column) -> bool:
    number_roll = 0
    if rolls[row][column] == 0:
        return False
    for dr in ROWS:
        for dc in COLUMNS:
            number_roll += get_value(rolls, row + dr, column + dc)
    if number_roll <= 4:
        return True
    return False

def part1(rolls: list[list[int]]) -> int:
    number_row = len(rolls)
    number_column = len(rolls[0])
    number_valid_row = 0
    for row in range(number_row):
        for column in range(number_column):
            if is_valid_roll(rolls, row, column):
                #print(f"Valid roll at row {row}, column {column}")
                number_valid_row += 1
    return number_valid_row

def part2(rolls: list[list[int]]) -> int:
    number_row = len(rolls)
    number_column = len(rolls[0])
    valid_position = []
    number_valid_row = 0
    for row in range(number_row):
        for column in range(number_column):
            if is_valid_roll(rolls, row, column):
                #print(f"Valid roll at row {row}, column {column}")
                valid_position.append((row, column))
                number_valid_row += 1
    for row, column in valid_position:
        rolls[row][column] = 0
    if number_valid_row == 0:
        return 0
    return number_valid_row + part2(rolls)


if __name__ == "__main__":
    data = EXEMPLE_DATA
    data = read_data(INPUT_FILE)
    #print(data)
    rolls = parse_data(data)
    #print(rolls)
    result_part1 = part1(rolls)
    print(f"Result part 1: {result_part1}")
    result_part2 = part2(rolls)
    print(f"Result part 2: {result_part2}")
