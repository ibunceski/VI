import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from datasets.zad8_dataset import dataset


def calculate(testset, train1, train2, train3, model, col):
    train_set = train1 + train2 + train3
    if col != -1:
        train_set = [row[:col] + row[(col + 1):] for row in train_set]
    trainx = [row[:-1] for row in train_set]
    trainy = [row[-1] for row in train_set]

    if col != -1:
        testset = [row[:col] + row[(col + 1):] for row in testset]
    testx = [row[:-1] for row in testset]
    testy = [row[-1] for row in testset]

    classifier = ...
    if model == "NB":
        classifier = GaussianNB()
    else:
        classifier = MLPClassifier(hidden_layer_sizes=50, activation="relu", learning_rate_init=0.001, random_state=0)
    classifier.fit(trainx, trainy)
    predictions = classifier.predict(testx)

    return accuracy_score(testy, predictions)


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=ConvergenceWarning)
    model = input()
    col = int(input())

    dataset1 = [row for row in dataset if row[-1] == 1]
    dataset0 = [row for row in dataset if row[-1] == 0]

    p1 = dataset0[:int(0.25 * len(dataset0))] + dataset1[:int(0.25 * len(dataset1))]
    p2 = dataset0[int(0.25 * len(dataset0)):int(0.5 * len(dataset0))] + dataset1[int(0.25 * len(dataset1)):int(0.5 * len(dataset1))]
    p3 = dataset0[int(0.5 * len(dataset0)):int(0.75 * len(dataset0))] + dataset1[int(0.5 * len(dataset1)):int(0.75 * len(dataset1))]
    p4 = dataset0[int(0.75 * len(dataset0)):] + dataset1[int(0.75 * len(dataset1)):]

    accuracies = []
    accuracies.append(calculate(p1, p2, p3, p4, model, -1))
    accuracies.append(calculate(p2, p1, p3, p4, model, -1))
    accuracies.append(calculate(p3, p2, p1, p4, model, -1))
    accuracies.append(calculate(p4, p2, p3, p1, model, -1))

    max_acc = accuracies.index(max(accuracies)) + 1
    final = ...
    if max_acc == 1:
        final = calculate(p1, p2, p3, p4, model, col)
    elif max_acc == 2:
        final = calculate(p2, p1, p3, p4, model, col)
    elif max_acc == 3:
        final = calculate(p3, p2, p1, p4, model, col)
    elif max_acc == 4:
        final = calculate(p4, p2, p3, p1, model, col)

    res = 0
    for acc in accuracies:
        res += acc

    res = res / 4

    print(f'Prosechna tochnost: {res}')
    print(f'Tochnost so otstraneta kolona: {max(accuracies)}')
