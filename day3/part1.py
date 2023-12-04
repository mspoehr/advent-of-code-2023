import re
import sys

filename = sys.argv[1]

schematic: list[str] = []
with open(filename) as f:
    for line in f:
        schematic.append(line.strip())


def is_symbol(str: str) -> bool:
    return str != "." and not str.isdecimal()


def surrounding_positions(row: int, span: tuple[int, int]) -> list[int]:
    return [
        (y, x)
        for x in range(span[0] - 1, span[1] + 1)
        for y in range(row - 1, row + 2)
        if y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[row])
    ]


def is_part_number(row: int, span: tuple[int, int]) -> bool:
    for position in surrounding_positions(row, span):
        if is_symbol(schematic[position[0]][position[1]]):
            return True


part_numbers = []
for index, row in enumerate(schematic):
    possible_part_numbers = re.finditer(r"\d+", row)
    for number in possible_part_numbers:
        if is_part_number(index, number.span()):
            part_numbers.append(int(number.group()))

print(sum(part_numbers))
