#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip().split("\n")
  for i, measurement in enumerate(data):
    l, w, h = map(int, measurement.split("x"))
    data[i] = (l, w, h)
  return data

def part_one(data):
  total = 0
  for l, w, h in data:
    sides = (l * w, l * h, w * h)
    sa = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
    total += sa + min(sides)
  return total

def part_two(data):
  total = 0
  for l, w, h in data:
    l, w, h = sorted((l, w, h))
    ribbon = 2 * l + 2 * w
    ribbon += (l * w * h)
    total += ribbon

  return total

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 02")
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
