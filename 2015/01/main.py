#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip().split("\n")
  data = data[0]
  return data

def part_one(data):
  floor = 0
  for move in data:
    if move == "(":
      floor += 1
    elif move == ")":
      floor -= 1
    else:
      raise ValueError(f"Unknown move: `{move}`")
  return floor

def part_two(data):
  floor = 0
  for i, move in enumerate(data, start = 1):
    if move == "(":
      floor += 1
    elif move == ")":
      floor -= 1
    else:
      raise ValueError(f"Unknown move: `{move}`")
    if floor < 0:
      return i

  raise Exception("no solution found")

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 01")
  print("-------------")

  print("Parsing input . . .")
  start = time.perf_counter_ns()
  data = parse_input(filename)
  end = time.perf_counter_ns()
  print(f"Completed in {utils.fmt_time(end - start)}.\n")

  print("Running solvers . . .\n")
  utils.run("Part One", part_one, data)
  utils.run("Part Two", part_two, data)

if __name__ == "__main__":
  main()
