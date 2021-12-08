#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip()
  data = list(map(int, data.split(",")))
  return data

def part_one(data):
  furthest = max(data)
  closest = min(data)

  min_cost = 2**64
  for i in range(closest, furthest + 1):
    cost = sum(abs(i - crab) for crab in data)
    if cost < min_cost:
      min_cost = cost

  return min_cost

def part_two(data):
  T = lambda n: n * (n + 1) // 2
  furthest, closest = max(data), min(data)
  min_cost = 2**64
  for i in range(closest, furthest + 1):
    cost = sum(T(abs(i - crab)) for crab in data)
    if cost < min_cost:
      min_cost = cost

  return min_cost

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 07")
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
