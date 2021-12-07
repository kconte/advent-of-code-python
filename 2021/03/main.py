#!/usr/bin/env python3

import sys
import time

import utils

bits = 5

def parse_input(filename):
  global bits
  with open(filename) as f:
    data = f.read().strip().split("\n")
  bits = len(data[0])
  return data

def reduce_search_space(data, bit, op):
  if len(data) == 1:
    return data
  data_len = len(data)
  half = data_len // 2 if data_len % 2 == 0 else data_len // 2 + 1
  count = 0
  for item in data:
    if item[bit] == "1":
      count += 1

  if op(count, half):
    keep = "1"
  else:
    keep = "0"

  func = lambda x: x[bit] == keep
  data = list(filter(func, data))
  return data

def part_one(data):
  counts = [0] * bits
  for bit in range(bits):
    count = sum(1 for item in data if item[bit] == "1")
    counts[bit] = count

  half = len(data) // 2
  gamma = 0
  mask = 0

  for count in counts:
    gamma <<= 1
    mask = (mask << 1) + 1
    if count >= half:
      gamma += 1

  epsilon = gamma ^ mask
  return gamma * epsilon

def part_two(data):
  O2 = data.copy()
  CO2 = data.copy()

  for bit in range(bits):
    O2 = reduce_search_space(O2, bit, lambda a, b: a >= b)
  oxygen = int(O2[0], 2)

  for bit in range(bits):
    CO2 = reduce_search_space(CO2, bit, lambda a, b: a < b)
  co2 = int(CO2[0], 2)

  return oxygen * co2

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 03")
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
