INPUT_FILE = "day6.txt"
EXAMPLE_DATE = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  "
]

def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.rstrip('\n') for line in file]

def parse_data(data: list[str]) -> list[list[int|str]]:
    simplified_data = []
    for line in data[:-1]:
        simplified_data.append([int(item) for item in line.split(' ') if item != ''])
    simplified_data.append([item for item in data[-1].split(' ') if item != ''])
    return simplified_data

def parse_data_2(data: list[str]) -> list[list[str]]:
    operations_temp = data[-1].split(' ')
    operations = []
    number_characters = []
    results = []

    for operation in operations_temp:
        if operation != '':
            number_characters.append(1)
            operations.append(operation)
            continue
        number_characters[-1] += 1

    print(operations)
    print(number_characters)

    for line in data[:-1]:
        line_items = []
        start_split = 0
        for number_c in number_characters:
            line_items.append(line[start_split:start_split+number_c])
            start_split += number_c + 1
        print(f"Line: '{line_items}'")
        results.append(line_items)

    results.append(operations)
    return results

def part1(data: list[list[int|str]]):
    operations = data[-1]
    number_rows = len(data) - 1
    number_columns = len(operations)
    results = []

    for row in range(number_rows):
        for column in range(number_columns):
            if row == 0:
                results.append(data[row][column])
                continue
            op = operations[column]
            if op == '+':
                results[column] += data[row][column]
            elif op == '*':
                results[column] *= data[row][column]
        print(results)

    print(f"Results: {results}")

    return sum(results)

def part2(data: list[list[str]]):

    print(data)

    operations = data[-1]
    number_rows = len(data) - 1
    number_columns = len(operations)
    results = []

    for column in range(number_columns):
        temp_numbers = []
        for row in range(number_rows):
            if row == 0:
                for c in str(data[row][column]):
                    temp_numbers.append(c)
                continue
            for index, c in enumerate(data[row][column]):
                temp_numbers[index] = temp_numbers[index] + c

        final_number = int(temp_numbers[0])
        for n in temp_numbers[1:]:
            op = operations[column]
            if op == '+':
                final_number += int(n)
            elif op == '*':
                final_number *= int(n)
        results.append(final_number)
        print(results)

    print(f"Results: {results}")

    return sum(results)

if __name__ == "__main__":
    data = EXAMPLE_DATE
    data = read_data(INPUT_FILE)
    parsed_data = parse_data(data)
    result_part1 = part1(parsed_data)
    print(f"Part 1: {result_part1}")

    parsed_data = parse_data_2(data)
    result_part2 = part2(parsed_data)
    print(f"Part 2: {result_part2}")
