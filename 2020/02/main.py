#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")
  for i, item in enumerate(data):
    item = item.split()
    a, b = map(int, item[0].split("-"))
    data[i] = (a, b, item[1][0], item[2])

  return data

def part_one(data):
  count = 0
  for a, b, c, s in data:
    if a <= s.count(c) <= b:
      count += 1
  return count

def part_two(data):
  count = 0
  for a, b, c, s in data:
    if (s[a - 1] == c) != (s[b - 1] == c):
      count += 1
  return count

def main():
  print()
  print("[XXXX] Day XX")
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
