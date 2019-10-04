'''
You are given 3 integers L, D, and X:

  - Determine the minimal integer N such that L <= N <= D and the sum of its
    digits is X
  - Determine the maximal integer M such that L <= M <= D and the sum of its
    digits is X

Input:
  - Three lines: L, D, X

Output:
  - Two lines: N, M
'''
import sys

# Read numbers L, D and X
numbers = [int(x) for x in sys.stdin]
L = numbers[0]
D = numbers[1]
X = numbers[2]

# Find numbers whose digits sum to X
sum_equals_X = []
for n in range(L, D+1):
    n_str = str(n)
    if (sum([int(c) for c in n_str]) == X):
        sum_equals_X.append(n)

# Sort digits whose sum equals X
sum_equals_X.sort()

# N = first item in list, M = last
N = sum_equals_X[0]
M = sum_equals_X[-1]

# Print N and M
print(N)
print(M)
