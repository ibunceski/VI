import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings

from datasets.zad5_dataset import dataset
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    dataset_1 = [row for row in dataset if row[-1] == 1]
    dataset_0 = [row for row in dataset if row[-1] == 0]

    train_set = [row for row in dataset_0[:int(0.8 * len(dataset_0))]] \
                + [row for row in dataset_1[:int(0.8 * len(dataset_1))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_set = [row for row in dataset_0[int(0.8 * len(dataset_0)):]] \
              + [row for row in dataset_1[int(0.8 * len(dataset_1)):]]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    learning_rate = float(input())
    epochs = int(input())

    classifier = MLPClassifier(6, activation="tanh", max_iter=epochs, learning_rate_init=learning_rate, random_state=0)
    classifier.fit(train_x, train_y)

    predictions_test = classifier.predict(train_x)
    predictions_val = classifier.predict(val_x)

    accuracy_test = accuracy_score(train_y, predictions_test)
    accuracy_val = accuracy_score(val_y, predictions_val)

    if accuracy_test > accuracy_val * 1.15:
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    print(f'Tochnost so trenirachko mnozhestvo: {accuracy_test}')
    print(f'Tochnost so validacisko mnozhestvo: {accuracy_val}')
