import re
import sys

filename = sys.argv[1]


with open(filename) as f:
    cards = f.readlines()

# we always have at least one of every card
scratchcards = {index: 1 for index in range(len(cards))}

for index, card in enumerate(cards):
    winning_numbers = list(map(int, re.findall(r"\d+", card.split("|")[0].split(":")[1])))
    card_numbers = list(map(int, re.findall(r"\d+", card.split("|")[1])))

    matches = len([x for x in card_numbers if x in winning_numbers])

    if matches > 0:
        for cloned_index in range(index + 1, index + matches + 1):
            if cloned_index < len(cards):
                scratchcards[cloned_index] += scratchcards[index]

print(sum(scratchcards.values()))
