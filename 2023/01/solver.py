import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver
import re

regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
convert_table = {
    "one":   "1",
    "1":     "1",
    "two":   "2",
    "2":     "2",
    "three": "3",
    "3":     "3",
    "four":  "4",
    "4":     "4",
    "five":  "5",
    "5":     "5",
    "six":   "6",
    "6":     "6",
    "seven": "7",
    "7":     "7",
    "eight": "8",
    "8":     "8",
    "nine":  "9",
    "9":     "9"
}

def parse_input(input):
    return input.split("\n")

def solve_part1(data):
    result = 0
    for line in data:
        matches = re.findall(r'\d', line)
        result += int(matches[0] + matches[-1])
    return result

def solve_part2(data):
    result = 0
    for line in data:
        matches = re.findall(regex, line)
        result += int(convert_table[matches[0]] + convert_table[matches[-1]])
    return result

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
