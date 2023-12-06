import sys

filename = sys.argv[1]


def digits_only(input: str) -> int:
    return int("".join(char for char in input if char.isdigit()))


with open(filename) as f:
    time = digits_only(f.readline())
    distance = digits_only(f.readline())


def calculate_distance_travelled(race_duration: int, charge_time: int) -> int:
    return (race_duration - charge_time) * charge_time


number_of_winning_charge_times = 0
for charge_time in range(1, time - 1):
    if calculate_distance_travelled(time, charge_time) > distance:
        number_of_winning_charge_times += 1

print(number_of_winning_charge_times)
