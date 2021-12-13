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
    if line[0] != "start" and line[1] != "end":
      append_or_default(data, line[1], line[0])

  return data

def bfs(graph, src, dst, node_check):
  paths = 0
  path = []
  queue = Queue()
  path.append(src)
  queue.enqueue(path)

  while queue:
    path = queue.dequeue()
    last = path[-1]

    if last == dst:
      paths += 1
      continue

    for child in graph[last]:
      if node_check(graph, path, child):
        new_path = path.copy() + [child]
        queue.enqueue(new_path)


  return paths

def histogram(xs):
  def inc_or_def(d, k):
    if k in d:
      d[k] += 1
    else:
      d[k] = 1

  histo = {}
  for x in xs:
    inc_or_def(histo, x)

  return histo

def part_one(data):
  def node_check(graph, path, node):
    return not (node in path and node.islower())

  paths = bfs(data, "start", "end", node_check)
  return paths

def part_two(data):
  def node_check(graph, path, node):
    smalls = [k for k in graph if k.islower() and k not in ["start", "end"]]
    counts = histogram([n for n in path if n in smalls])
    if node == "start":
      return False
    elif node not in counts:
      return True
    elif counts[node] == 1 and (len([(k, v) for k, v in counts.items() if k != node and v == 2]) == 0):
      return True
    return False

  paths = bfs(data, "start", "end", node_check)

  return paths

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
