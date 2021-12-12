#!/usr/bin/env python3

import copy
import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n")

  data = [
    list(map(int, list(line))) for line in raw
  ]
  return data

def print_data(data, end = ""):
  for row in data:
    row = "".join([str(item) for item in row])
    print(row)
  print("", end = end)

def get_neighbors(i, j, n):
  return list(
    filter(lambda pos: 0 <= pos[0] < n and 0 <= pos[1] < n,
      [
        (i - 1, j - 1), # upper left
        (i - 1, j),     # upper
        (i - 1, j + 1), # upper right
        (i, j - 1),     # left
        (i, j + 1),     # right
        (i + 1, j - 1), # lower left
        (i + 1, j),     # lower
        (i + 1, j + 1)  # lower right
      ]
    )
  )

def simulate(data, neighbors):
  N = len(data)
  flashed = set()

  def flash(i, j):
    if (i, j) in flashed:
      return
    if data[i][j] <= 9:
      return

    flashed.add((i, j))
    for y, x in neighbors[(i, j)]:
      data[y][x] += 1
    for y, x in neighbors[(i, j)]:
      flash(y, x)

  # first, increase all energy levels by 1
  for i in range(N):
    for j in range(N):
      data[i][j] += 1

  # do the flashes
  for i in range(N):
    for j in range(N):
      flash(i, j)

  # reset flashed
  for i, j in flashed:
    data[i][j] = 0

  return len(flashed)

def part_one(data):
  grid = copy.deepcopy(data)
  N = len(grid)
  neighbors = {
    (i, j): get_neighbors(i, j, N) for i in range(N) for j in range(N)
  }

  flashes = 0
  for i in range(100):
    flashes += simulate(grid, neighbors)

  return flashes

def part_two(data):
  grid = copy.deepcopy(data)
  N = len(grid)
  neighbors = {
    (i, j): get_neighbors(i, j, N) for i in range(N) for j in range(N)
  }

  i = 0
  while True:
    flashes = simulate(grid, neighbors)
    i += 1
    if flashes == 100:
      break

  return i

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 11")
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
