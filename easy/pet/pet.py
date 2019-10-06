'''
Background:
    - Five contestants compete in preparing culinary delights.
    - Every evening, one of them makes dinner and each of the other four
      grades it on a scale from 1 to 5.
    - Number of points a contestant gets is equal to the sum of the grades
      they got.
    - Winner is the contestant who gets the most points.

Problem:
    - Write a program to determine the winner and how many points they got

Input:
    - Five lines:
        - Each line contains 4 integers
        - The contestants are numbered 1 to 5 in the order the lines
          are given
        * Input guarentees a unique solution

Output:
    - A single line:
        - The winners number and their points, separated by a space
'''
def get_winner_and_score(scores_list):
    winner, winning_score = 0, 0
    for contestant, scores in enumerate(scores_list):
        score = sum(scores)
        if score > winning_score:
            winning_score = score
            winner = contestant+1
    return winner, winning_score

def get_scores_from_data(data):
    scores = []
    for raw_scores in data:
        tokenized = raw_scores.split()
        int_scores = list(map((lambda x: int(x)), tokenized))
        scores.append(int_scores)
    return scores

def main():
    import sys

    # Read lines
    data = sys.stdin.readlines()

    # Get scores
    scores = get_scores_from_data(data)

    # Get winner and winning score
    winner, score = get_winner_and_score(scores)

    # Print winner and winning score
    print(str(winner) + ' ' + str(score))

if __name__ == '__main__':
    main()
