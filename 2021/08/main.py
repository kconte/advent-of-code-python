#!/usr/bin/env python3

import functools
import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n")

  data = []
  for line in raw:
    patterns, outputs = line.split("|")
    patterns = sorted(patterns.strip().split(), key = lambda s: len(s))
    for i, pattern in enumerate(patterns):
      pattern = "".join(sorted(pattern))
      patterns[i] = pattern

    outputs = outputs.strip().split()
    for i, output in enumerate(outputs):
      output = "".join(sorted(output))
      outputs[i] = output
    data.append((patterns, outputs))

  return data

def derive(signals):
  code = dict()
  one = signals[0]
  seven = signals[1]
  four = signals[2]
  eight = signals[-1]

  code[one] = 1
  code[four] = 4
  code[seven] = 7
  code[eight] = 8

  four_diff = "".join([c for c in four if c not in one])

  signals = signals[3:-1]
  five_segs, six_segs = signals[:3], signals[3:]
  for signal in five_segs:
    if all(c in signal for c in one):
      code[signal] = 3
    elif all(c in signal for c in four_diff):
      code[signal] = 5
    else:
      code[signal] = 2

  for signal in six_segs:
    if all(c in signal for c in four):
      code[signal] = 9
    elif all(c in signal for c in four_diff):
      code[signal] = 6
    else:
      code[signal] = 0

  return code

def part_one(data):
  count = 0
  for _, output in data:
    for word in output:
      #                  1  7  4  8
      if len(word) in [2, 3, 4, 7]:
        count += 1

  return count

def part_two(data):
  total = 0
  for signals, outputs in data:
    code = derive(signals)
    val = 0
    for i, output in enumerate(outputs):
      val *= 10
      val += code[output]
    total += val

  return total

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 08")
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
