#!/usr/bin/env python3

import sys
import time

from squeue import Queue
import utils

def append_or_default(d: dict, k, v):
  if k in d.keys():
    d[k].append(v)
  else:
    d[k] = [v]

def print_dict(d: dict):
  print("{")
  for k, v in d.items():
    print(f"  {k}: {v}")
  print("}")

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n")

  data = {}
  for line in raw:
    line = line.split("-")
    append_or_default(data, line[0], line[1])
    append_or_default(data, line[1], line[0])

  return data

def bfs(graph, src, dst):
  paths = []
  queue = Queue()
  path = []
  path.append(src)
  queue.enqueue(path)

  while queue:
    path = queue.dequeue()
    last = path[-1]

    if last == dst:
      paths.append(path.copy())
      continue

    for child in graph[last]:
      if child in path and child.islower():
        continue
      new_path = path.copy() + [child]
      queue.enqueue(new_path)

  return paths

def bfs_modified(graph, src, dst):
  paths = []
  path = []
  queue = Queue()
  path.append(src)
  queue.enqueue(path)

  while queue:
    path = queue.dequeue()

    if path[-1] == dst:
      paths.append(path.copy())
      continue

    for child in graph[path[-1]]:
      pass

  return paths


def part_one(data):
  paths = bfs(data, "start", "end")
  return len(paths)

def part_two(data):
  paths = bfs_modified(data, "start", "end")

  for path in paths:
    print(" -> ".join(path))

  raise Exception("no solution found")

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 12")
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
