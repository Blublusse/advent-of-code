import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

def has_special_char_adjacent(matrix, x, y):
    min_x = max(0, x-1)
    max_x = min(len(matrix[0]) - 1, x+1)
    min_y = max(0, y-1)
    max_y = min(len(matrix) - 1, y+1)
    for xx in range(min_x, max_x + 1):
        for yy in range(min_y, max_y + 1):
            char = matrix[yy][xx]
            if type(char) == str:
                return True
    return False

def get_adjacent_numbers(matrix, x, y):
    result = []
    min_y = max(0, y-1)
    max_y = min(len(matrix) - 1, y+1)
    for yy in range(min_y, max_y + 1):
        line = matrix[yy]
        current_number = ""
        count_number = False
        for xx, char in enumerate(line):
            if type(char) == int:
                current_number += str(char)
                if xx >= x-1 and xx <= x+1 and y >= y-1 and y <= y+1:
                    count_number = True
            if xx == len(line) - 1 or type(line[xx+1]) != int:
                if count_number:
                    result.append(int(current_number))
                current_number = ""
                count_number = False
    return result

def parse_input(input):
    result = []
    for line in input.split("\n"):
        line_result = []
        for char in line:
            value = False
            if char.isnumeric():
                value = int(char)
            elif not char == '.':
                value = char
            line_result.append(value)
        result.append(line_result)
    return result

def solve_part1(data):
    result = 0
    for y, line in enumerate(data):
        current_number = ""
        count_number = False
        for x, char in enumerate(line):
            if type(char) == int:
                current_number += str(char)
                if has_special_char_adjacent(data, x, y):
                    count_number = True
            if x == len(line) - 1 or type(line[x+1]) != int:
                if count_number:
                    result += int(current_number)
                current_number = ""
                count_number = False
    return result

def solve_part2(data):
    result = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '*':
                adjacent_numbers = get_adjacent_numbers(data, x, y)
                if len(adjacent_numbers) == 2:
                    result += adjacent_numbers[0] * adjacent_numbers[1]
    return result

solver = AOCSolver(DIR, parse_input, solve_part1, solve_part2)
solver.test()
solver.solve()
