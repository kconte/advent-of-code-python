#!/usr/bin/env python3

import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip()

  raw = map(int, raw.split(","))
  data = [0] * 9
  for fish in raw:
    data[fish] += 1

  return data

def update_population(population):
  new_population = [0] * 9
  for i in range(8, 0, -1):
    new_population[i - 1] = population[i]
  new_population[8] += population[0]
  new_population[6] += population[0]
  return new_population

def part_one(data):
  population = data.copy()
  print(population)
  for _ in range(80):
    population = update_population(population)
    print(population)
  return sum(population)

def part_two(data):
  population = data.copy()
  for _ in range(256):
    population = update_population(population)
  return sum(population)

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 06")
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
