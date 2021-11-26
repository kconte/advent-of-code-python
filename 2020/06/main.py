#!/usr/bin/env python3

import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n\n")
  return data

def part_one(data):
  count = 0
  for group in data:
    group = group.replace("\n", "")
    count += len(set(group))
  return count

def part_two(data):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  count = 0
  for group in data:
    group = group.split()
    for c in alphabet:
      if all(c in p for p in group):
        count += 1
  return count

def main():
  print()
  print("[2020] Day 06")
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
