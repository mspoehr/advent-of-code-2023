import re
import sys

from collections import defaultdict

filename = sys.argv[1]

schematic: list[str] = []
with open(filename) as f:
    for line in f:
        schematic.append(line.strip())


def is_gear(str: str) -> bool:
    return str == "*"


def surrounding_positions(row: int, span: tuple[int, int]) -> list[int]:
    return [
        (y, x)
        for x in range(span[0] - 1, span[1] + 1)
        for y in range(row - 1, row + 2)
        if y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[row])
    ]


def adjacent_gears(row: int, span: tuple[int, int]) -> list[tuple[int, int]]:
    adjacent_gears = []
    for position in surrounding_positions(row, span):
        if is_gear(schematic[position[0]][position[1]]):
            adjacent_gears.append(position)

    return adjacent_gears


possible_gears = defaultdict(list)
part_numbers = []

for index, row in enumerate(schematic):
    possible_part_numbers = re.finditer(r"\d+", row)
    for number in possible_part_numbers:
        gears = adjacent_gears(index, number.span())
        for gear in gears:
            possible_gears[gear].append(int(number.group()))

gear_ratio_coefficients = filter(lambda adjacent_parts: len(adjacent_parts) == 2, possible_gears.values())
gear_ratios = [coeff1 * coeff2 for coeff1, coeff2 in gear_ratio_coefficients]

print(sum(gear_ratios))
