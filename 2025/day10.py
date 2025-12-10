from typing import Tuple
import z3

INPUT_FILE = "2025/day10.txt"
EXAMPLE_DATA = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]


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


def parse_data(data: list[str]) -> list[Tuple[str, list[list[int]], list[int]]]:
    """_summary_

    Args:
        data (list[str]): _description_

    Returns:
        list[tuple[str, list[int], list[tuple[int, int]], list[int]]]: _description_
    """
    parsed = []
    for line in data:
        parts = line.split(" ")
        indicator = parts[0].strip("[]")
        joltage = [int(c) for c in parts[-1].strip("{})").split(",") if c]
        buttons = []
        for p in parts[1:-1]:
            buttons.append([int(c) for c in p.strip("()").split(",") if c])
        parsed.append((indicator, buttons, joltage))
     
    return parsed


def part1(data: list[Tuple[str, list[list[int]], list[int]]]) -> int:
    """_summary_

    Args:
        data (list[tuple[str, list[int], list[tuple[int, int]], list[int]]]): _description_

    Returns:
        int: _description_
    """
    
    #print(data)
    result = 0

    for target, buttons, _ in data:
        todo = ['.' * len(target)]
        handled = set(todo)
        steps = 0

        while True:
            steps += 1

            assert(len(todo) > 0)

            new_states = set()

            for state in todo:
                state = list(state)
                for b in buttons:
                    ns = state[:]
                    for p in b:
                        ns[p] = '.' if ns[p] == '#' else '#'
                    ns = ''.join(ns)
                    new_states.add(ns)

            if target in new_states:
                result += steps
                break

            todo = new_states - handled
            handled.update(new_states)

    return result


def part2(data: list[Tuple[str, list[list[int]], list[int]]]) -> int:
    """_summary_

    Args:
        data (list[tuple[str, list[int], list[tuple[int, int]], list[int]]]): _description_

    Returns:
        int: _description_
    """
    result = 0

    for (_, buttons, joltage) in data:
        o = z3.Optimize()

        button_vars = []

        for b in range(len(buttons)):
            bv = z3.Int(f'button{b}')
            button_vars.append(bv)
            o.add(bv >= 0)

        for jidx, j in enumerate(joltage):
            jeq = sum(bv
                      for b, bv
                      in zip(buttons, button_vars)
                      if jidx in b)

            o.add(jeq == j)

        steps = z3.Int('steps')
        o.add(steps == sum(button_vars))

        o.minimize(steps)
        o.check()

        result += o.model()[steps].as_long()

    return result


if __name__ == "__main__":
    data = EXAMPLE_DATA
    data = read_data(INPUT_FILE)
    parsed_data = parse_data(data)
    result_part1 = part1(parsed_data)
    print(f"Part 1: {result_part1}")
    result_part2 = part2(parsed_data)
    print(f"Part 2: {result_part2}")