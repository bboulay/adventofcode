from typing import List, Tuple

INPUT_FILE = "day5.txt"
EXEMPLE_DATA = ["3-5", "10-14", "16-20", "12-18", "", "1", "5", "8", "11", "17", "32"]

def read_data(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def parse_data(data: list[str]) -> Tuple[list[tuple[int, int]], list[int]]:
    fresh_ranges = []
    product_ids = []
    for line in data:
        if line.strip() == "":
            continue
        # we are in range
        if "-" in line:
            start, end = line.split("-")
            fresh_ranges.append((int(start), int(end)))
            continue
        product_ids.append(int(line.strip()))
    return fresh_ranges, product_ids

def part1(fresh_ranges: list[tuple[int, int]], product_ids: list[int]) -> int:
    total_fresh = 0
    for product_id in product_ids:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= product_id <= end:
                is_fresh = True
                break
        if is_fresh:
            total_fresh += 1
    return total_fresh

def part2(fresh_ranges: list[tuple[int, int]]) -> int:
    total_fresh = 0
    fresh_ranges = sorted(fresh_ranges)
    print(fresh_ranges)
    clean_ranges = [fresh_ranges[0]]
    for start, end in fresh_ranges[1:]:
        clean_start, clean_end = clean_ranges[-1]
        if start > clean_end:
            clean_ranges.append((start, end))
        else:
            new_start, new_end = clean_ranges[-1]
            new_end = max(clean_end, end)
            clean_ranges[-1] =(new_start, new_end)
    print(clean_ranges)
    for start, end in clean_ranges:
        total_fresh += end - start + 1

    return total_fresh

if __name__ == "__main__":
    data = EXEMPLE_DATA
    data = read_data(INPUT_FILE)
    fresh_ranges, product_ids = parse_data(data)
    result_part1 = part1(fresh_ranges, product_ids)
    print("Part 1: ", result_part1)
    result_part2 = part2(fresh_ranges)
    print("Part 2: ", result_part2)
