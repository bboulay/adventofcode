from typing import Any, Generator

INPUT_FILE = "day3.txt"
EXEMPLE_DATA = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

def read_data(input_file: str) -> list[str]:
    with open(input_file, "r") as file:
        return [line.strip() for line in file]

def bank_to_list(bank: str) -> list[int]:
    return [int(char) for char in bank]

def part1(banks: list[str]) -> int:
    joltage = 0
    for bank in banks:
        batteries = bank_to_list(bank)

        first_digit = max(batteries)
        index_first_digit = batteries.index(first_digit)

        if index_first_digit == len(batteries) - 1 :
            second_digit = first_digit
            first_digit = max(batteries[:index_first_digit])
        else:
            second_digit = max(batteries[index_first_digit+1:])
        highest_joltage = first_digit * 10 + second_digit

        #print(bank, highest_joltage)
        joltage += highest_joltage

    return joltage

def get_max_digits(batteries: list[int], number_digit: int) -> list[int]:
    #print(batteries, number_digit)
    if number_digit == 1:
        return [max(batteries)]

    number_batteries = len(batteries)
    if number_digit == number_batteries + 1:
        # check first and second
        first_digit = max(batteries[:2])
        result = batteries[:2]
        result.insert(0, first_digit)
        #print("return: ", result)
        return result

    sub_batteries = batteries[0: number_batteries - number_digit + 1]
    digit = max(sub_batteries)
    index_digit = sub_batteries.index(digit)
    result = get_max_digits(batteries[index_digit+1:], number_digit -1)
    result.insert(0, digit)
    return result


def part2(banks: list[str]) -> int:
    joltage = 0
    number_digit = 12

    for bank in banks:
        batteries = bank_to_list(bank)
        max_digits = get_max_digits(batteries, number_digit)
        #print(bank, max_digits)
        for index, digit in enumerate(max_digits):
            joltage += digit * (10 ** (number_digit - index -1))

    return joltage

if __name__ == "__main__":
    data = EXEMPLE_DATA
    data = read_data(INPUT_FILE)
    result_part1 = part1(data)
    print(f"Part 1: {result_part1}")
    result_part2 = part2(data)
    print(f"Part 2: {result_part2}")
