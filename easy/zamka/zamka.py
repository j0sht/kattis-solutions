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

# Let N (the min) be the max possible value, and M the min possible
N = D
M = L

# Find numbers whose digits sum to X, find N and M in the process
for n in range(L, D+1):
    n_str = str(n)
    if (sum([int(c) for c in n_str]) == X):
        if n < N:
            N = n
        if n > M:
            M = n

# Print N and M
print(N)
print(M)
