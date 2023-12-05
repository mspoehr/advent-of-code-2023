import sys

filename = sys.argv[1]

almanac_maps: dict[str, list[tuple[int, int, int]]] = {}

with open(filename, "r") as file:
    initial_seeds = list(map(int, file.readline().split(":")[1].strip().split(" ")))

    for line in file:
        if "map:" in line:
            map_name = line.split(" ")[0]
            almanac_maps[map_name] = []
        elif line != "\n":
            almanac_maps[map_name].append(tuple(map(int, line.split(" "))))


def convert(conversion: str, value: int) -> int:
    ranges = almanac_maps[conversion]

    for converted_range in ranges:
        dest_start, src_start, length = converted_range
        if value >= src_start and value < src_start + length:
            return dest_start + (value - src_start)

    return value


locations: list[int] = []

for seed in initial_seeds:
    for conversion in almanac_maps.keys():
        seed = convert(conversion, seed)

    locations.append(seed)


print(min(locations))
