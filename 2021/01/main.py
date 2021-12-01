#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")
  data = list(map(int, data))
  return data

def count_increases(data):
  increases = 0
  for a, b in zip(data[:-1], data[1:]):
    if b > a:
      increases += 1
  return increases

def part_one(data):
  return count_increases(data)

def part_two(data):
  windows = [data[i:i + 3] for i in range(len(data) - 2)]
  measurements = [sum(window) for window in windows]
  return count_increases(measurements)

def main():
  print()
  print("[2021] Day 01")
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
