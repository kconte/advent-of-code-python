#!/usr/bin/env python3

import bitarray
import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip().split("\n")

  for i, item in enumerate(data):
    item = item.split()
    if item[0] == "toggle":
      sx, sy = map(int, item[1].split(","))
      ex, ey = map(int, item[3].split(","))
      data[i] = (item[0], sx, sy, ex, ey)
    else:
      sx, sy = map(int, item[2].split(","))
      ex, ey = map(int, item[4].split(","))
      data[i] = (item[1], sx, sy, ex, ey)

  return data

def part_one(data):
  N = 1000
  lights = bitarray.bitarray(N * N)
  lights.setall(0)

  for cmd, sx, sy, ex, ey in data:
    for y in range(sy, ey + 1):
      start = y * N + sx
      stop = y * N + ex + 1
      if cmd == "toggle":
        lights[start:stop] = ~lights[start:stop]
      elif cmd == "on":
        lights[start:stop] = 1
      else:
        lights[start:stop] = 0

  return sum(lights)

def part_two(data):
  N = 1000
  lights = [0] * (N * N)

  for cmd, sx, sy, ex, ey in data:
    for y in range(sy, ey + 1):
      for x in range(sx, ex + 1):
        i = y * N + x
        if cmd == "toggle":
          lights[i] += 2
        elif cmd == "off":
          lights[i] = max(lights[i] - 1, 0)
        else:
          lights[i] += 1

  return sum(lights)

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 06")
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
