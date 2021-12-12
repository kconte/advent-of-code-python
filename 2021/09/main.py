#!/usr/bin/env python3

import queue
import sys
import time

import utils

# def part_two(data):

#   def get_basin(idx: int, basin: set, neighbors: queue.Queue):
#     if idx in basin:
#       return
#     elif idx < 0 or idx >= data_len:
#       return
#     elif data[idx] == 9:
#       return

#     print(idx)
#     basin.add(idx)
#     for i in [idx + 1, idx - 1, idx + N, idx - N]:
#       if i not in basin:
#         neighbors.put(i)

#     while not neighbors.empty():
#       n = neighbors.get()
#       get_basin(n, basin, neighbors)

#   basin = set()
#   get_basin(0, basin, queue.Queue())
#   print(basin)

#   raise Exception("no solution found")

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n")
  data = [
    list(map(int, list(row))) for row in raw
  ]
  return data

def get_neighbors(i, j, M, N):
  return list(
    filter(
      lambda pos: 0 <= pos[0] < M and 0 <= pos[1] < N,
      [
        (i, j - 1),
        (i, j + 1),
        (i - 1, j),
        (i + 1, j)
      ]
    )
  )

def part_one(data):
  M = len(data)
  N = len(data[0])
  vals = list()

  for i in range(M):
    for j in range(N):
      val = data[i][j]
      if all(val < data[y][x] for y, x in get_neighbors(i, j, M, N)):
        vals.append(val)

  return sum(1 + val for val in vals)

def part_two(data):

  # data = [
  #   [0, 1, 2, 9, 4],
  #   [0, 1, 2, 9, 4],
  #   [9, 1, 2, 9, 4],
  #   [9, 9, 9, 9, 4],
  #   [4, 4, 4, 4, 4],
  # ]

  M = len(data)
  N = len(data[0])

  pts = set()
  basins = list()


  def get_basin(i, j, basin: set):
    if (i, j) in basin:
      return
    elif data[i][j] == 9:
      return
    basin.add((i, j))
    for y, x in get_neighbors(i, j, M, N):
      get_basin(y, x, basin)

  for i in range(M):
    for j in range(N):
      if (i, j) in pts:
        continue
      basin = set()
      get_basin(i, j, basin)
      if len(basin) > 0:
        basins.append(basin)
        for pt in basin:
          pts.add(pt)

  basin_sizes = [len(basin) for basin in sorted(basins, key = lambda xs: len(xs), reverse = True)]

  return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 09")
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
