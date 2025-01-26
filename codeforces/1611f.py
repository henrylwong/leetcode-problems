#!/usr/bin/env python3

import sys

def atm_and_students(n, starting_balance, arr):
  start = 0
  cur_balance = starting_balance
  max_length, best_start, best_end = 0, -1, -1

  for end in range(n):
    cur_balance += arr[end]

    while start <= end and cur_balance < 0:
      cur_balance -= arr[start]
      start += 1

    cur_length = end - start + 1 
    if cur_length > max_length:
      max_length = cur_length
      best_start, best_end = start + 1, end + 1
 
  if max_length > 0:
    return f"{best_start} {best_end}"
  return "-1"

def solve():
  input = sys.stdin.read
  data = input().splitlines()
  
  t = int(data[0])  # Number of test cases
  results = []
  idx = 1
  
  for _ in range(t):
    n, s = map(int, data[idx].split())  # Read n (number of students) and s (initial ATM balance)
    a = list(map(int, data[idx + 1].split()))  # Read the array of transactions
    idx += 2

    results.append(atm_and_students(n, s, a)) 

  # Print all results
  sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
  solve()