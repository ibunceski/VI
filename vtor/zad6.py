import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from datasets.zad6_dataset import dataset
from sklearn.metrics import accuracy_score, precision_score

if __name__ == "__main__":
    X = int(input())
    criteria = 'gini'

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = [row for row in dataset[:(len(dataset) - X)]]
    train_x = [row[:-1] for row in train_set]
    train_x_enc = encoder.transform(train_x)
    train_y = [row[-1] for row in train_set]

    test_set = [row for row in dataset[(len(dataset) - X):]]
    test_x = [row[:-1] for row in test_set]
    test_x_enc = encoder.transform(test_x)
    test_y = [row[-1] for row in test_set]

    classifier = DecisionTreeClassifier(criterion=criteria, random_state=0)
    classifier.fit(train_x_enc, train_y)

    predictions = classifier.predict(test_x_enc)

    # tp, fp, tn, fn = 0, 0, 0, 0
    #
    # for pred, real in zip(predictions, test_y):
    #     if pred == '0' and real == '0':
    #         tn += 1
    #     elif pred == '0' and real == '1':
    #         fn += 1
    #     elif pred == '1' and real == '0':
    #         fp += 1
    #     elif pred == '1' and real == '1':
    #         tp += 1
    # accuracy = 0.0 if (tn+tp) == 0 else tp + tn / (tp + fp + tn + fn)
    # precision = 0.0 if (tp + fp) == 0 else tp / (tp + fp)

    print(f'Accuracy: {accuracy_score(test_y, predictions)}')
    print(f'Precision: {precision_score(test_y, predictions, pos_label="1", zero_division=0)}')
