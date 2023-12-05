import sys

from itertools import product

filename = sys.argv[1]

almanac_maps: dict[str, list[tuple[range, int]]] = {}

with open(filename, "r") as file:
    seed_tuple_list = map(int, file.readline().split(":")[1].strip().split(" "))
    iterator = iter(seed_tuple_list)
    seed_ranges = [range(start, start + length) for start, length in zip(iterator, iterator)]

    for line in file:
        if "map:" in line:
            map_name = line.split(" ")[0]
            almanac_maps[map_name] = []
        elif line.startswith("#"):
            pass
        elif line != "\n":
            dest_start, src_start, length = map(int, line.split(" "))
            almanac_maps[map_name].append((range(src_start, src_start + length), dest_start - src_start))

max_input = max([seed_range.stop for seed_range in seed_ranges])

for mapping in almanac_maps.values():
    mapping.sort(key=lambda tuple: tuple[0].start)  # sort mapping tuples by input values ascending

    extra_mappings = []

    for index, (input_range, diff) in enumerate(mapping):
        if index < len(mapping) - 1 and input_range.stop != mapping[index + 1][0].start:
            extra_mappings.append((range(input_range.stop, mapping[index + 1][0].start), 0))

    if mapping[0][0].start != 0:
        extra_mappings.append((range(0, mapping[0][0].start), 0))

    if mapping[-1][0].stop <= max_input:
        extra_mappings.append((range(mapping[-1][0].stop, max_input + 1), 0))
    else:
        max_input = mapping[-1][0].stop - 1

    mapping.extend(extra_mappings)


def range_intersection(range1: range, range2: range) -> range:
    return range(max(range1.start, range2.start), min(range1.stop, range2.stop))


def possible_outputs(input_ranges: list[range], output_mappings: list[tuple[range, int]]) -> list[range]:
    combinations = product(input_ranges, output_mappings)

    possible_outputs: list[range] = []

    for input_range, (mapped_range, diff) in combinations:
        intersection = range_intersection(input_range, mapped_range)

        if len(intersection) > 0:
            possible_outputs.append(range(intersection.start + diff, intersection.stop + diff))

    return possible_outputs


last_output_ranges = seed_ranges
for name, mapping in almanac_maps.items():
    last_output_ranges = possible_outputs(last_output_ranges, mapping)

last_output_ranges.sort(key=lambda range: range.start)
print(last_output_ranges[0].start)
