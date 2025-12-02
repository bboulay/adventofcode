INPUT_FILE = "day2.txt"
EXEMPLE_DATA = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def read_data(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read().strip()

def parse_data(data: str) -> list[tuple[int, int]]:
    entries = data.split(",")
    return [parse_entry(entry) for entry in entries]

def parse_entry(entry: str) -> tuple[int, int]:
    start, end = entry.split("-")
    return int(start), int(end)

def is_invalid(product_id: int) -> bool:
    product_id_str = str(product_id)
    product_id_length = len(product_id_str)
    #print(product_id, product_id_length, product_id_length % 2)
    if product_id_length % 2 != 0:
        return False
    middle = int(product_id_length/2)
    first_part = product_id_str[:middle]
    second_part = product_id_str[middle:]
    #print(product_id_str, first_part, second_part)
    return first_part == second_part

def part1(product_ids: list[tuple[int, int]]) -> int:
    counter = 0
    for start,end in product_ids:
        #print(start, end)
        for product_id in range(start, end + 1):
            if is_invalid(product_id):
                #print(f"{product_id} is invalid")
                counter += product_id
    return counter

def is_invalid_part2(product_id: int) -> bool:
    product_id_str = str(product_id)
    product_id_length = len(product_id_str)
    #print(product_id, product_id_length, product_id_length % 2)

    # need to check 0, 1, ..., middle characters are repeated
    for i in range(int(product_id_length/2)):
        number_to_check = product_id_str[0:i+1]
        length_to_check = len(number_to_check)
        if product_id_length % length_to_check != 0:
            continue
        repeated_number = number_to_check * int(product_id_length / length_to_check)
        #print("to check: ", i, number_to_check, int(repeated_number), product_id)
        if int(repeated_number) == product_id:
            return True

    return False

def part2(product_ids: list[tuple[int, int]]) -> int:
    counter = 0
    for start,end in product_ids:
        #print("Range: ", start, end)
        for product_id in range(start, end + 1):
            if is_invalid_part2(product_id):
                #print(f"{product_id} is invalid")
                counter += product_id
    return counter

if __name__ == "__main__":
    data = EXEMPLE_DATA
    data = read_data(INPUT_FILE)
    print(data)
    product_ids = parse_data(data)
    result_part1 = part1(product_ids)
    print(f"Part 1 result: {result_part1}")
    result_part2 = part2(product_ids)
    print(f"Part 2 result: {result_part2}")
