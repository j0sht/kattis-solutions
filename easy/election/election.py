'''
link to problem: https://open.kattis.com/problems/election2
'''
import sys

candidate_party = dict()
candidate_votes = dict()

data = sys.stdin.readlines()
num_candidates = int(data.pop(0))
for i in range(0, num_candidates):
    candidate = data.pop(0).strip()
    party = data.pop(0).strip()
    candidate_party[candidate] = party

num_votes = int(data.pop(0))
max_vote = 0
winner = ''
for i in range(0, num_votes):
    candidate = data.pop(0).strip()
    if candidate_votes.get(candidate):
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1
    candidates_vote_total = candidate_votes[candidate]
    if candidates_vote_total >= max_vote:
        if winner == '':
            winner = candidate
        else:
            if candidate != winner:
                if max_vote == candidates_vote_total:
                    winner = 'tie'
                else:
                    winner = candidate
        max_vote = candidates_vote_total

if winner == 'tie':
    print(winner)
else:
    print(candidate_party[winner])
