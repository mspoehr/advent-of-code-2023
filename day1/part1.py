import sys


filename = sys.argv[1]


calibration_values = []
with open(filename, "r") as file:
    for line in file:
        calibration_values.append(line)


def find_first_digit(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return int(string[i])
    return None


def find_last_digit(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            return int(string[i])
    return None


sum = 0
for calibration_value in calibration_values:
    first_integer = find_first_digit(calibration_value)
    last_integer = find_last_digit(calibration_value)

    sum += first_integer * 10 + last_integer

print(sum)
