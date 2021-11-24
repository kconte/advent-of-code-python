#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")
  data = sorted(list(map(int, data)))
  return data

def part_one(data):

  for i, x in enumerate(data):
    for y in data[i + 1:]:
      if x + y == 2020:
        return x * y

  raise Exception("no solution found")

def part_two(data):

  for i, x in enumerate(data):
    for j, y in enumerate(data[i + 1:], i + 1):
      for z in data[j + 1:]:
        if x + y + z == 2020:
          return x * y * z

  raise Exception("no solution found")

def main():
  print()
  print("[2020] Day 01")
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
