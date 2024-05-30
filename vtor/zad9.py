import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score, recall_score
from datasets.zad9_dataset import dataset

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    x = int(input())

    train_set = [row for row in dataset[:(len(dataset) - x)]]
    trainx = [row[:-1] for row in train_set]
    trainy = [row[-1] for row in train_set]
    test_set = [row for row in dataset[(len(dataset) - x):]]
    testx = [row[:-1] for row in test_set]
    testy = [row[-1] for row in test_set]

    classifier = MLPClassifier(3, activation='relu', learning_rate_init=0.003, max_iter=200, random_state=0)
    classifier.fit(trainx, trainy)
    predictions = classifier.predict(testx)

    print(f'Precision: {precision_score(testy, predictions, zero_division=0)}')
    print(f'Recall: {recall_score(testy, predictions, zero_division=0)}')
