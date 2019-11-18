import random
from typing import TypeVar, List, Tuple

#use a typevar to represent what is a data point
X = TypeVar('X')

# this function will split the data in fractions [p, 1 - p]
def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    data = data[:] #shallow copy
    random.shuffle(data)
    cut = int(len(data) * prob)
    return data[:cut], data[cut:]

# running tests
data = [n for n in range(1000)]

train, test = split_data(data, 0.75)
assert len(train) == 750
assert len(test) == 250

assert sorted(train + test) == data
