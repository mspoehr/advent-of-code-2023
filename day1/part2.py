import sys
from typing import Callable, Optional


filename = sys.argv[1]

letter_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

calibration_values: list[str] = []
with open(filename, "r") as file:
    for line in file:
        calibration_values.append(line)


def __find_index_of_integer(string: str, start: int, end: int, step: int) -> Optional[int]:
    for i in range(start, end, step):
        if string[i].isdigit():
            return i
    return None


def find_index_of_first_integer(string: str) -> Optional[int]:
    return __find_index_of_integer(string, 0, len(string), 1)


def find_index_of_last_integer(string: str) -> Optional[int]:
    return __find_index_of_integer(string, len(string) - 1, -1, -1)


def __find_position_of_digit(
    string: str, search: Callable[[str], int], test: Callable[[int, int], bool]
) -> tuple[Optional[int], int]:
    position = None
    length = 0

    for digit in letter_digits.keys():
        index = search(digit)
        if index != -1 and (position is None or test(index, position)):
            position = index
            length = len(digit)

    return position, length


def find_position_of_first_letter_digit(string: str) -> tuple[Optional[int], int]:
    return __find_position_of_digit(string, string.find, lambda index, position: index < position)


def find_position_of_last_letter_digit(string: str) -> tuple[Optional[int], int]:
    return __find_position_of_digit(string, string.rfind, lambda index, position: index > position)


def find_first_digit(string):
    index = find_index_of_first_integer(string)
    position, length = find_position_of_first_letter_digit(string)

    if position is not None and (index is None or position < index):
        return letter_digits[string[position : position + length]]

    return int(string[index])


def find_last_digit(string):
    index = find_index_of_last_integer(string)
    position, length = find_position_of_last_letter_digit(string)

    if position is not None and (index is None or position > index):
        return letter_digits[string[position : position + length]]

    return int(string[index])


sum = 0
for calibration_value in calibration_values:
    first_integer = find_first_digit(calibration_value)
    last_integer = find_last_digit(calibration_value)

    sum += first_integer * 10 + last_integer

print(sum)
