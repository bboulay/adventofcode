from typing import Any, Generator

INPUT_FILE = "day1.txt"
START_POINT = 50
EXAMPLE_DATA = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]

def read_data(filename: str) -> Generator[str, Any, None]:
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

def parse_entry(entry: str) -> tuple[str, int]:
    direction = entry[0]
    value = int(entry[1:])
    return direction, value

def compute_next_position(current_position: int, direction: str, value: int) -> int:
    if direction == "L":
        value = (int(value / 100) + 1) * 100 - value

    current_position = current_position + value
    current_position = current_position % 100

    return current_position

def compute_next_position_and_number_zero(current_position: int, direction: str, value: int) -> tuple[int, int]:
    count_zero = 0
    if direction == "L":
        value = -value

    current_position = (current_position + value) % 100

    count_zero += current_position // 100

    if current_position == 0:
        count_zero += 1
    if value > 0 and current_position < (value % 100) and current_position != 0:
        count_zero += 1
    if value < 0 and current_position > 100 - (abs(value) % 100):
        count_zero += 1
    count_zero += abs(value) // 100

    return current_position, count_zero

def example_exercise1() -> None:
    count_zero = 0
    current_position = 50
    for entry in EXAMPLE_DATA:
        direction, value = parse_entry(entry)
        current_position = compute_next_position(current_position, direction, value)
        if current_position == 0:
            count_zero += 1

    print(f"Count of zero part 1 (example): {count_zero}")

def exercise1() -> None:
    count_zero = 0
    current_position = START_POINT
    for entry in read_data(INPUT_FILE):
        direction, value = parse_entry(entry)
        current_position = compute_next_position(current_position, direction, value)
        if current_position == 0:
            count_zero += 1

    print(f"Count of zero part 1: {count_zero}")

def example_exercise2() -> None:
    count_zero = 0
    current_position = START_POINT
    for entry in EXAMPLE_DATA:
        direction, value = parse_entry(entry)
        current_position, add_zero = compute_next_position_and_number_zero(current_position, direction, value)
        count_zero += add_zero

    print(f"Count of zero part 2 (example): {count_zero}")

def exercise2() -> None:
    count_zero = 0
    current_position = START_POINT
    for entry in read_data(INPUT_FILE):
        direction, value = parse_entry(entry)
        current_position, add_zero = compute_next_position_and_number_zero(current_position, direction, value)
        count_zero += add_zero

    print(f"Count of zero part 2: {count_zero}")


if __name__ == "__main__":
    example_exercise1()
    exercise1()
    example_exercise2()
    exercise2()
