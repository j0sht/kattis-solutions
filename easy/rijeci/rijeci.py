'''
Background:
    - Starting with the letter A, a button is pushed and the A
      is replaced with a B
    - The next time the button is pushed, the word changes to BA
    - There after, the pattern continues each time the button is
      pressed, with all the letters B getting transformed to BA,
      and all the letters A get transformed to B.

Problem:
    - After K times of pressing the button, how many letters A and
      how many letters B will be displayed on the screen?

Input:
    - The first line of input contains the integer 1 <= K <= 45,
      the number of time the button is pushed

Output:
    - The first and only line of output must contain two
      space-separated integers, the number of letters A and the
      number of letters B.
'''
def last_two_fib(n):
    second_last, last = 0, 1
    for i in range(2, n+1):
        new = second_last + last
        second_last = last
        last = new
    return second_last, last

def main():
    import sys
    K = int(sys.stdin.readline())
    num_a, num_b = last_two_fib(K)
    output = str(num_a) + ' ' + str(num_b)
    print(output)
    
if __name__ == "__main__":
    main()
