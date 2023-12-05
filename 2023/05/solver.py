import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

def parse_input(input):
    result = {
        "seeds": [],
        "maps": []
    }
    lines = input.split("\n")
    result["seeds"] = lines.pop(0).split(":")[1].split()
    current_map = {}
    for line in lines:
        if "map" in line:
            if current_map:
                result["maps"].append(current_map.copy())
                current_map = {}
        elif line:
            line_split = line.split()
            dest_start = int(line_split[0])
            source_start = int(line_split[1])
            length = int(line_split[2])
            for i in range(length):
                current_map[str(source_start+i)] = str(dest_start+i)
    return result

def solve_part1(data):
    result = 0
    converted_seeds = data["seeds"].copy()
    for map in data["maps"]:
        for i, seed in enumerate(converted_seeds):
            converted_seeds[i] = map[seed] if seed in map else seed
    result = min(converted_seeds)
    return result

def solve_part2(data):
    return "None"

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
