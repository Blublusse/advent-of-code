from abc import abstractmethod
import os
class AOCSolver:

  def __init__(self, dir):
    self.dir = dir

  @abstractmethod
  def parse_input(self, input):
    raise NotImplementedError

  @abstractmethod
  def solve_part1(self, data):
    raise NotImplementedError

  @abstractmethod
  def solve_part2(self, data):
    raise NotImplementedError

  def solve(self):
    puzzle1_input = (self.dir / "input1.txt").read_text().strip()
    solution1 = self.solve_part1(self.parse_input(puzzle1_input))
    print("solution 1 : \033[38;5;3m" + str(solution1) + "\033[0;0m")

    puzzle2_input = (self.dir / "input2.txt").read_text().strip()
    solution2 = self.solve_part2(self.parse_input(puzzle2_input))
    print("solution 2 : \033[38;5;3m" + str(solution2) + "\033[0;0m")

  def test(self):
    for part in [1,2]:
      for file in os.listdir(self.dir / "examples/" / str(part)):
        if "input" in file:
          example = file[0:2]
          example1_input = (self.dir / "examples" / str(part) / file).read_text().strip()
          example1_solution = self.solve_part1(self.parse_input(example1_input))
          solution_file = file[0:2] + "_solution.txt"
          example1_expected_solution = (self.dir / "examples" / str(part) / solution_file).read_text().strip()
          print("[test] " + str(part) + "/" + example + " : " + ("\033[38;5;2mOK\033[0;0m" if str(example1_solution) == example1_expected_solution else "\033[38;5;1mNOK\033[0;0m"))
