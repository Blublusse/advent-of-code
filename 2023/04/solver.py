import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

import re

def get_card_values(data):
    result = []
    for card in data:
        matches = 0
        for picked_number in card[1]:
            if picked_number in card[0]:
                matches += 1
        result.append(matches)
    return result

def parse_input(input):
    result = []
    for line in input.split("\n"):
        number_groups = line.split(": ")[1].split(" | ")
        winning_numbers = []
        for winning_number in number_groups[0].split():
            winning_numbers.append(int(winning_number))
        picked_numbers = []
        for picked_number in number_groups[1].split():
            picked_numbers.append(int(picked_number))
        result.append([
            winning_numbers,
            picked_numbers
        ])
    return result

def solve_part1(data):
    result = 0
    for matches in get_card_values(data):
        if matches:
            result += 1 << (matches-1)
    return result

def solve_part2(data):
    result = 0
    raw_card_values = get_card_values(data)
    collected_card_quantities = [1] * len(raw_card_values)
    while raw_card_values:
        raw_card_value = raw_card_values.pop(0)
        card_quantity = collected_card_quantities.pop(0)
        result += 1 + card_quantity * raw_card_value
        for c in range(card_quantity):
            for i in range(raw_card_value):
                collected_card_quantities[i] += 1
    return result

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
