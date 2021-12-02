#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip().split("\n")
  return data


def part_one(data):
  def is_nice(s):
    # counting vowels
    vcount = 0
    for vowel in "aeiou":
      vcount += s.count(vowel)

    if vcount < 3:
      return False

    # looking for pairs
    found = False
    for i, c in enumerate(s[:-1]):
      if c == s[i + 1]:
        found = True
        break

    if not found:
      return False

    # looking for invalid pairs
    for pair in ["ab", "cd", "pq", "xy"]:
      if pair in s:
        return False

    return True

  count = 0
  for s in data:
    if is_nice(s):
      count += 1
  return count

def part_two(data):
  def is_nice(s):
    slen = len(s)

    # repeating, non-overlapping pairs
    valid = False
    for i in range(slen - 3):
      pair = s[i:i + 2]
      for j in range(i + 2, slen - 1):
        if pair == s[j:j + 2]:
          valid = True
          break
      if valid:
        break
    if not valid:
      return False

    # same char, separated by another
    for i in range(slen - 2):
      if s[i] == s[i + 2]:
        return True

    return False

  count = 0
  for s in data:
    if is_nice(s):
      count += 1

  return count

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2015] Day 05")
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
