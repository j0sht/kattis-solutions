'''
Problem:

  - Cell provider allows you to use up to X mb of data each month.

  - Each mb not spent that month gets transferred to the next.

  - Given the number of months N, determine how many mb you will have
    available in the N+1th month


Input:

  - First line: X, second line: N, following N lines: Pi where Pi is
    the number of mb spent in each of the first N months. Pi will
    never use more mb than available.

Output:

  - Number of mb available in the N+1th month

'''
import sys

# Read numbers
numbers = [int(x) for x in sys.stdin]
X = numbers[0]
mbs_used = numbers[2:]

# Calculate mbs remaining in each of the first N months
mbs_remaining = [X - Pi for Pi in mbs_used]

# Print number of mbs available in month N+1
mbs_available = sum(mbs_remaining) + X
print(mbs_available)
