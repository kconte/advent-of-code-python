#!/usr/bin/env python3

from functools import reduce
import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")
  return data

def count_trees(pattern, slope = (3, 1)):
  i, j = 0, 0
  count = 0
  while i < len(pattern):
    if pattern[i][j] == "#":
      count += 1

    j = (j + slope[0]) % len(pattern[0])
    i += slope[1]
  return count


def part_one(data):
  return count_trees(data)

def part_two(data):
  trees = [
    count_trees(data, (1, 1)),
    count_trees(data, (3, 1)),
    count_trees(data, (5, 1)),
    count_trees(data, (7, 1)),
    count_trees(data, (1, 2)),
  ]
  return reduce(lambda x, y: x * y, trees)

def main():
  print()
  print("[2020] Day 03")
  print("-------------")

  print("Parsing input . . .")
  start = time.perf_counter_ns()
  data = parse_input()
  end = time.perf_counter_ns()
  print(f"Completed in {utils.fmt_time(end - start)}.\n")

  print("Running solvers . . .\n")
  utils.run("Part One", part_one, data)
  utils.run("Part Two", part_two, data)

if __name__ == "__main__":
  main()
