import sys

filename = sys.argv[1]

almanac_maps: dict[str, dict[int, int]] = {}


def process_almanac_mapping(dest_map: dict[int, int], line) -> None:
    dest_range_start, source_range_start, length = map(int, line.split(" "))

    for i in range(length):
        dest_map[source_range_start + i] = dest_range_start + i


with open(filename, "r") as file:
    initial_seeds = list(map(int, file.readline().split(":")[1].strip().split(" ")))

    for line in file:
        if "map:" in line:
            map_name = line.split(" ")[0]
            almanac_maps[map_name] = {}
        elif line != "\n":
            process_almanac_mapping(almanac_maps[map_name], line)


def convert(conversion: str, value: int) -> int:
    map = almanac_maps[conversion]
    if value in map:
        return map[value]
    else:
        return value


locations: list[int] = []

for seed in initial_seeds:
    for conversion in almanac_maps.keys():
        seed = convert(conversion, seed)

    locations.append(seed)


print(min(locations))
