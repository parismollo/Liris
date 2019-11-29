from resources.linear_algebra import Vector, distance
import tqdm
from typing import List
import random

def random_point(dim: int) -> Vector:
    return [random.random() for _ in range(dim)]

def random_distances(dim: int, num_pairs: int) -> List[float]:
    return [distance(random_point(dim), random_point(dim))
    for _ in range(num_pairs)]

dimensions = range(1, 101)
avg_distances = []
min_distances = []

random.seed(0)

for dim in tqdm.tqdm(dimensions, desc="Curse of Dimensionality"):
    distances = random_distances(dim, 10000)
    avg_distances.append(sum(distances) / 10000)
    min_distances.append(min(distances))

min_avg_ratio = [min_dist / avg_dist
 for min_dist, avg_dist in zip(min_distances, avg_distances)]
