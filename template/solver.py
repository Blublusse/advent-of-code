import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

def parse_input(input):
    return "None"

def solve_part1(data):
    return "None"

def solve_part2(data):
    return "None"

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
