import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

max_by_color = {
    "red":   12,
    "green": 13,
    "blue":  14
}

def parse_input(input):
    result = []
    for line in input.split("\n"):
        if not line.strip():
            continue
        sets = []
        for set in line.split(": ")[1].split("; "):
            set_result = {}
            for color in set.split(", "):
                color_split = color.split(" ")
                set_result[color_split[1]] = int(color_split[0])
            sets.append(set_result)
        result.append(sets)
    return result

def solve_part1(data):
    result = 0
    for game_index, game in enumerate(data):
        game_possible = True
        for set in game:
            for color in set:
                if int(set[color]) > max_by_color[color]:
                    game_possible = False
                    break
            if not game_possible:
                break
        if not game_possible:
            continue
        result += game_index + 1
    return result

def solve_part2(data):
    result = 0
    for game in data:
        game_min = { "red": 0, "green": 0, "blue": 0 }
        for set in game:
            for color in set:
                game_min[color] = max(game_min[color], set[color])
        game_power = 1
        for min in game_min:
            game_power *= game_min[min]
        result += game_power
    return result

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
