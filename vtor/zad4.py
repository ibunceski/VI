import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from datasets.zad4_dataset import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    col_to_remove = int(input())
    num_trees = int(input())
    criterion = input()
    test_input = list(map(float, input().split(" ")))
    test_input = test_input[:col_to_remove] + test_input[(col_to_remove + 1):]

    train_set = [row[:col_to_remove] + row[(col_to_remove + 1):] for row in dataset[:int(0.85 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = [row[:col_to_remove] + row[(col_to_remove + 1):] for row in dataset[int(0.85 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_trees, criterion=criterion, random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)

    print(f"Accuracy: {accuracy_score(test_y, predictions)}")
    print(classifier.predict([test_input])[0])
    print(classifier.predict_proba([test_input])[0])
