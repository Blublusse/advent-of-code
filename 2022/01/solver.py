import pathlib
import sys
DIR = pathlib.Path(__file__).parent
sys.path.append(str(DIR.parent.parent))
from lib.aoc_solver import AOCSolver

class Solver(AOCSolver):
    
    def parse_input(self, input):
        data = []
        for group in input.split("\n\n"):
            group_data = []
            for element in group.split("\n"):
                if element:
                    group_data.append(int(element))
            data.append(group_data)
        return data

    def solve_part1(self, data):
        result = 0
        for group in data:
            group_result = 0
            for element in group:
                group_result += element
            result = max(result, group_result)
        return result

    def solve_part2(self, data):
        return "None"

solver = Solver(DIR)
solver.test()
solver.solve()
