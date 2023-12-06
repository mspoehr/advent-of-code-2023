import sys
import operator
import functools

filename = sys.argv[1]


def read_integers(input: str) -> list[int]:
    return [int(x) for x in input.split(" ") if x != ""]


with open(filename) as f:
    times = read_integers(f.readline().split(":")[1].strip())
    distances = read_integers(f.readline().split(":")[1].strip())


def calculate_distance_travelled(race_duration: int, charge_time: int) -> int:
    return (race_duration - charge_time) * charge_time


races = zip(times, distances)
number_of_winning_charge_times = []

for time, distance in races:
    record_charge_times = []
    for charge_time in range(1, time - 1):
        if calculate_distance_travelled(time, charge_time) > distance:
            record_charge_times.append(charge_time)

    number_of_winning_charge_times.append(len(record_charge_times))

print(functools.reduce(operator.mul, number_of_winning_charge_times))
