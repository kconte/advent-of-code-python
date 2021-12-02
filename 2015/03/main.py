#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip()
  return data

def part_one(data):
  visited = set()
  x, y = 0, 0
  visited.add((x, y))
  for move in data:
    if move == "^":
      y += 1
    elif move == "v":
      y -= 1
    elif move == "<":
      x -= 1
    elif move == ">":
      x += 1
    else:
      raise ValueError(f"Unknown command: `{move}`")
    visited.add((x, y))
  return len(visited)

def part_two(data):
  visited = set()
  sx, sy, rx, ry = 0, 0, 0, 0
  visited.add((sx, sy))
  for i, move in enumerate(data):
    x, y = 0, 0
    if move == "^":
      y = 1
    elif move == "v":
      y = -1
    elif move == "<":
      x = -1
    elif move == ">":
      x = 1
    else:
      raise ValueError(f"Unknown command: `{move}`")
    if i % 2 == 0:
      sx += x
      sy += y
      visited.add((sx, sy))
    else:
      rx += x
      ry += y
      visited.add((rx, ry))

  return len(visited)

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 03")
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
