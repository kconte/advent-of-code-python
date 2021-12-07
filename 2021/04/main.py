#!/usr/bin/env python3

import copy
import sys
import time

import utils

def parse_input(filename):
  with open(filename) as f:
    raw = f.read().strip().split("\n\n")

  draws = list(map(int, raw[0].strip().split(",")))
  boards = list()

  for raw_board in raw[1:]:
    numbers = list(map(int, raw_board.split()))
    boards.append(numbers)

  data = (draws, boards)
  return data

def check_for_winner(boards):
  N = 5
  for idx, board in enumerate(boards):
    # check left/right
    for i in range(N):
      si = i * N
      if board[si:si + N] == [None] * N:
        return idx

    # check up/down
    for j in range(N):
      col = [board[i * N + j] for i in range(N)]
      if col == [None] * N:
        return idx

  return None

def remove_winners(boards):

  N = 5
  idxes = set()
  for idx, board in enumerate(boards):
    # check left/right
    for i in range(N):
      si = i * N
      if board[si:si + N] == [None] * N:
        idxes.add(idx)

    # check up/down
    for j in range(N):
      col = [board[i * N + j] for i in range(N)]
      if col == [None] * N:
        idxes.add(idx)

  if len(boards) == 1 and len(idxes) == 1:
    return (boards, True)

  return [board for i, board in enumerate(boards) if i not in idxes], False

def part_one(data):
  draws, boards = data[0], copy.deepcopy(data[1])
  for draw in draws:
    for board in boards:
      for i, val in enumerate(board):
        if val == draw:
          board[i] = None
    idx = check_for_winner(boards)
    if idx is not None:
      break
  
  board_sum = sum(filter(lambda x: x is not None, boards[idx]))
  return board_sum * draw

def part_two(data):
  draws, boards = data[0], copy.deepcopy(data[1])
  for draw in draws:
    for board in boards:
      for i, val in enumerate(board):
        if val == draw:
          board[i] = None
    boards, done = remove_winners(boards)
    if done:
      break

  board_sum = sum(filter(lambda x: x is not None, boards[0]))

  return board_sum * draw
    
def main():
  filename = "./input.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]

  print()
  print("[2021] Day 04")
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
