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
for i in range(0, num_votes):
    candidate = data.pop(0).strip()
    if candidate_votes.get(candidate):
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

votes = list(candidate_votes.values())
votes.sort(reverse=True)
if len(votes) > 1 and votes[0] == votes[1]:
    print("tie")
else:
    for candidate in candidate_votes:
        if candidate_votes[candidate] == votes[0]:
            print(candidate_party[candidate])
            break

