#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n")

  data = list()
  for line in raw:
    sp, ep = line.split(" -> ")
    sx, sy = map(int, sp.split(","))
    ex, ey = map(int, ep.split(","))
    data.append((sx, sy, ex, ey))

  return data

def part_one(data):
  pts = dict()

  for sx, sy, ex, ey in data:
    # vertical line
    if sx == ex:
      lower, upper = min(sy, ey), max(sy, ey)
      for y in range(lower, upper + 1):
        if (sx, y) in pts.keys():
          pts[(sx, y)] += 1
        else:
          pts[(sx, y)] = 1

    # horizontal line
    elif sy == ey:
      lower, upper = min(sx, ex), max(sx, ex)
      for x in range(lower, upper + 1):
        if (x, sy) in pts.keys():
          pts[(x, sy)] += 1
        else:
          pts[(x, sy)] = 1

  count = len(list(filter(lambda x: x > 1, pts.values())))
  return count

def part_two(data):
  pts = dict()

  for sx, sy, ex, ey in data:
    # vertical line
    if sx == ex:
      lower, upper = min(sy, ey), max(sy, ey)
      for y in range(lower, upper + 1):
        if (sx, y) in pts.keys():
          pts[(sx, y)] += 1
        else:
          pts[(sx, y)] = 1

    # horizontal line
    elif sy == ey:
      lower, upper = min(sx, ex), max(sx, ex)
      for x in range(lower, upper + 1):
        if (x, sy) in pts.keys():
          pts[(x, sy)] += 1
        else:
          pts[(x, sy)] = 1

    # diagonal line
    else:
      xdir = 1 if ex - sx > 0 else -1
      ydir = 1 if ey - sy > 0 else -1
      x, y = sx, sy
      for _ in range(abs(ex - sx) + 1):
        if (x, y) in pts:
          pts[(x, y)] += 1
        else:
          pts[(x, y)] = 1
        x += xdir
        y += ydir

  count = len(list(filter(lambda x: x > 1, pts.values())))
  return count

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 05")
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
