#!/usr/bin/env python3

import re
import time

import utils

def parse_input():
  with open("./input.txt") as f:
    data = f.read().strip().split("\n\n")

  for i, raw in enumerate(data):
    pairs = list(map(lambda s: s.split(":"), raw.split()))
    data[i] = {
      k: v for k, v in pairs
    }
    if data[i].get("cid"):
      del data[i]["cid"]

  return data

expected_keys = sorted([ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ])

def has_keys(passport):
  return sorted(passport.keys()) == expected_keys

def part_one(data):
  return sum(1 for passport in data if has_keys(passport))

def part_two(data):
  hexex = re.compile(r"^#[\da-f]{6}$")
  ecls = [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]
  pidex = re.compile(r"^\d{9}$")

  count = 0
  for passport in data:
    if not has_keys(passport):
      continue

    # byr
    if not "1920" <= passport["byr"] <= "2002":
      continue

    # iyr
    if not "2010" <= passport["iyr"] <= "2020":
      continue

    # eyr
    if not "2020" <= passport["eyr"] <= "2030":
      continue

    # hgt
    hgt = passport["hgt"]
    unit = hgt[-2:]
    val = int(hgt[:-2])
    if unit in ["in", "cm"]:
      if unit == "cm" and not 150 <= val <= 193:
        continue
      elif unit == "in" and not 59 <= val <= 76:
        continue
    else:
      continue

    # hcl
    if not hexex.match(passport["hcl"]):
      continue

    # ecl
    if not passport["ecl"] in ecls:
      continue

    # pid
    pid = passport["pid"]
    if not pidex.match(pid):
      continue

    count += 1

  return count

def main():
  print()
  print("[2020] Day 04")
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
