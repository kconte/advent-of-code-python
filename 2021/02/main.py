#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n")

  for i, item in enumerate(data):
    item = item.split()
    item[1] = int(item[1])
    data[i] = (item[0], item[1])

  return data

def part_one(data):
  pos, depth = 0, 0
  for inst, val in data:
    if inst == "forward":
      pos += val
    elif inst == "down":
      depth += val
    elif inst == "up":
      depth -= val
    else:
      raise ValueError(f"Unknown instruction: `{inst}`")
  return pos * depth

def part_two(data):
  pos, depth, aim = 0, 0, 0
  for inst, val in data:
    if inst == "forward":
      pos += val
      depth += aim * val
    elif inst == "down":
      aim += val
    elif inst == "up":
      aim -= val
    else:
      raise ValueError(f"Unknown instruction: `{inst}`")
  return pos * depth

def main():
  print()
  print("[2021] Day 02")
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
