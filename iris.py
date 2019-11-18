import requests
#
# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#
# with open('iris.data', 'w') as f:
#     f.write(data.text)

from typing import Dict, List, Tuple
import csv
from collections import defaultdict
from knearest import LabeledPoint
from resources.linear_algebra import Vector
from knearest import knn_classify


def parse_iris_row(row: List[str]) -> LabeledPoint:
    measurements = [float(value) for value in row[:-1]]
    label = row[-1].split("-")[-1]
    return LabeledPoint(measurements, label)

with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]

points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

def plot_scatter():
    from matplotlib import pyplot as plt
    metrics = ['sepal length', 'sepal width', 'petal length', 'petal width']
    pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
    marks = ['+', '.', 'x']

    fig, ax = plt.subplots(2, 3)

    for row in range(2):
        for col in range(3):
            i, j = pairs[3 * row + col]
            ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
            ax[row][col].set_xticks([])
            ax[row][col].set_yticks([])

            for mark, (species, points) in zip(marks, points_by_species.items()):
                xs = [point[i] for point in points]
                ys = [point[j] for point in points]
                ax[row][col].scatter(xs, ys, marker=mark, label=species)

    ax[-1][-1].legend(loc='lower right', prop={'size': 6})
    plt.show()


import random
from resources.splitter import split_data

def run_model():
    random.seed(12)
    iris_train, iris_test = split_data(iris_data, 0.70)
    assert len(iris_train) == 0.7 * 150
    assert len(iris_test) == 0.3 * 150

    confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)
    num_correct = 0

    for iris in iris_test:
        predicted = knn_classify(5, iris_train, iris.point)
        actual = iris.label

        if predicted  == actual:
            num_correct+=1
        confusion_matrix[(predicted, actual)]+=1

    pct_correct = num_correct/len(iris_test)
    print(pct_correct, confusion_matrix)

if __name__ == "__main__":
    print("Running model\n")
    run_model()
    print("Plotting scatter graph")
    plot_scatter()
