import re
import sys

filename = sys.argv[1]


points = 0
with open(filename) as f:
    for card in f:
        winning_numbers = list(map(int, re.findall(r"\d+", card.split("|")[0].split(":")[1])))
        card_numbers = list(map(int, re.findall(r"\d+", card.split("|")[1])))

        matches = len([x for x in card_numbers if x in winning_numbers])

        if matches > 0:
            points += pow(2, matches - 1)

print(points)
