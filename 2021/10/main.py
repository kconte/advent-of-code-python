#!/usr/bin/env python3

from os import error
import sys
import time

from stack import Stack
import utils

def parse_input(filename):
  with open(filename) as f:
    data = f.read().strip().split("\n")
  return data

def part_one(data):

  pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
  }

  scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
  }

  error_score = 0

  stack = Stack()
  for line in data:
    for c in line:
      if c in "([{<":
        stack.push(c)
      elif c in ")]}>":
        if pairs[stack.peek()] == c:
          stack.pop()
        else:
          error_score += scores[c]
          break

  return error_score

def part_two(data):

  pairs = {
    "(": ")", "[": "]",
    "{": "}", "<": ">",
  }

  scores = {
    ")": 1, "]": 2,
    "}": 3, ">": 4,
  }

  completion_scores = []

  stack = Stack()
  for line in data:
    for c in line:
      if c in "([{<":
        stack.push(c)
      elif c in ")]}>":
        if pairs[stack.peek()] == c:
          stack.pop()
        else:
          stack.sink()
          break
    if not stack.is_empty():
      score = 0
      completion_str = ""
      while not stack.is_empty():
        completion_str += pairs[stack.pop()]
      for c in completion_str:
        score *= 5
        score += scores[c]
      completion_scores.append(score)

  completion_scores = sorted(completion_scores)
  mid = len(completion_scores) // 2

  return completion_scores[mid]

def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 10")
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
