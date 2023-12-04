import re
import sys


filename = sys.argv[1]


class Game:
    def __init__(self, game_string: str) -> None:
        self.id = int(re.match("^Game (\\d+):", game_string).group(1))

        self.red_cubes = self.__parse_max_cubes(game_string, "red")
        self.blue_cubes = self.__parse_max_cubes(game_string, "blue")
        self.green_cubes = self.__parse_max_cubes(game_string, "green")

    def is_possible(self) -> bool:
        return self.red_cubes <= 12 and self.green_cubes <= 13 and self.blue_cubes <= 14

    def __parse_max_cubes(self, game_string: str, color: str) -> int:
        return max(map(int, re.findall(f"(\\d+) {color}", game_string)))


with open(filename, "r") as file:
    games: list[Game] = [Game(line) for line in file]

possible_games = filter(Game.is_possible, games)
sum_of_possible_ids = sum(map(lambda game: game.id, possible_games))


print(sum_of_possible_ids)
