import re
import sys


filename = sys.argv[1]


class Game:
    def __init__(self, game_string: str) -> None:
        self.id = int(re.match("^Game (\\d+):", game_string).group(1))

        self.min_red_cubes = self.__parse_max_cubes(game_string, "red")
        self.min_blue_cubes = self.__parse_max_cubes(game_string, "blue")
        self.min_green_cubes = self.__parse_max_cubes(game_string, "green")

    def power(self) -> int:
        return self.min_red_cubes * self.min_blue_cubes * self.min_green_cubes

    def __parse_max_cubes(self, game_string: str, color: str) -> int:
        return max(map(int, re.findall(f"(\\d+) {color}", game_string)))


with open(filename, "r") as file:
    games: list[Game] = [Game(line) for line in file]


game_power_sum = sum(map(Game.power, games))


print(game_power_sum)
