#!/usr/bin/env python3

import hashlib
import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip()
  return data

def irange(start = 1, step = 1):
  val = start
  while True:
    yield val
    val += 1

def search(data, match):
  rng = len(match)
  for i in irange():
    val = f"{data}{i}".encode()
    md5 = hashlib.md5(val).hexdigest()
    if md5[:rng] == match:
      return i

def part_one(data):
  return search(data, "00000")

def part_two(data):
  return search(data, "000000")

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 04")
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
