import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from datasets.zad7_dataset import dataset
from sklearn.metrics import precision_score


def get_split(dataset, mode, split):
    if mode == "balanced":
        d0 = [row for row in dataset if row[-1] == 0]
        d1 = [row for row in dataset if row[-1] == 1]

        train_set = [row for row in d0[:int(split * len(d0))]] + [row for row in d1[:int(split * len(d1))]]
        test_set = [row for row in d0[int(split * len(d0)):]] + [row for row in d1[int(split * len(d1)):]]
    else:
        train_set = [row for row in dataset[:int(split * len(dataset))]]
        test_set = [row for row in dataset[int(split * len(dataset)):]]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    return train_x, train_y, test_x, test_y


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=ConvergenceWarning)
    mode = input()
    split = int(input()) / 100

    train_x, train_y, test_x, test_y = get_split(dataset, mode, split)

    classifier1 = GaussianNB()
    classifier1.fit(train_x, train_y)
    predictions1 = classifier1.predict(test_x)

    classifier2 = RandomForestClassifier(n_estimators=50, criterion="entropy", random_state=0)
    classifier2.fit(train_x, train_y)
    predictions2 = classifier2.predict(test_x)

    classifier3 = MLPClassifier(hidden_layer_sizes=50, activation="relu", learning_rate_init=0.001, random_state=0)
    classifier3.fit(train_x, train_y)
    predictions3 = classifier3.predict(test_x)

    accuracy1, precision1 = classifier1.score(test_x, test_y), precision_score(test_y, predictions1, zero_division=0)
    accuracy2, precision2 = classifier2.score(test_x, test_y), precision_score(test_y, predictions2, zero_division=0)
    accuracy3, precision3 = classifier3.score(test_x, test_y), precision_score(test_y, predictions3, zero_division=0)

    precision_list = [precision1, precision2, precision3]
    max_precision = max(precision_list)

    if precision1 == max_precision:
        print(f'Najvisoka preciznost ima prviot klasifikator')
        print(f'Negovata tochnost e: {accuracy1}')
    elif precision2 == max_precision:
        print(f'Najvisoka preciznost ima vtoriot klasifikator')
        print(f'Negovata tochnost e: {accuracy2}')
    else:
        print(f'Najvisoka preciznost ima tretiot klasifikator')
        print(f'Negovata tochnost e: {accuracy3}')
