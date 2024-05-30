import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from datasets.zad3_dataset import dataset

if __name__ == "__main__":
    split = int(input())
    criterion = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = [row for row in dataset[int(((100 - split) / 100) * len(dataset)):]]
    train_x = [row[:-1] for row in train_set]
    train_x_enc = encoder.transform(train_x)
    train_y = [row[-1] for row in train_set]

    test_set = [row for row in dataset[:int(((100 - split) / 100) * len(dataset))]]
    test_x = [row[:-1] for row in test_set]
    test_x_enc = encoder.transform(test_x)
    test_y = [row[-1] for row in test_set]

    classifier = DecisionTreeClassifier(random_state=0, criterion=criterion)
    classifier.fit(train_x_enc, train_y)

    predictions = classifier.predict(test_x_enc)
    features = list(classifier.feature_importances_)

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")
    print(f"Accuracy: {accuracy_score(test_y, predictions)}")
    print(f"Most important feature: {features.index(max(features))}")
    print(f"Least important feature: {features.index(min(features))}")

