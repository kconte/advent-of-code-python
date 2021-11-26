#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")
  return data

def get_seatid(code):
  assert len(code) == 10

  u, l = 127, 0
  for c in code[:7]:
    if c == "F":
      u = (u - l) // 2 + l
    elif c == "B":
      l = (u - l) // 2 + l + 1
    else:
      raise ValueError(f"unknown char: `{c}`")
  assert l == u
  row = u

  u, l = 7, 0
  for c in code[7:]:
    if c == "L":
      u = (u - l) // 2 + l
    elif c == "R":
      l = (u - l) // 2 + l + 1
    else:
      raise ValueError(f"unknown char: `{c}`")
  assert l == u
  col = u

  return row * 8 + col

def part_one(data):
  return max(get_seatid(seat) for seat in data)

def part_two(data):
  seatids = sorted(get_seatid(seat) for seat in data)

  for i, seatid in enumerate(seatids):
      if seatids[i + 1] - seatid == 2:
          return seatid + 1

  raise Exception("no solution found")

def main():
  print()
  print("[2020] Day 05")
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
