from typing import List
from collections import Counter

# Let's pick a number k like 3 and then classify some new data point, we will look for the k nearest labeled points and let them vote
# however this won't be able to deal with ties...
def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

assert raw_majority_vote(['a','b','c','b']) == 'b'
