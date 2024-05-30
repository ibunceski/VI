import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from datasets.zad2_dataset import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    test_input = list(map(float, input().split(" ")))

    dataset = [[float(el) for el in row[:-1]] + [row[-1]] for row in dataset]

    train_set = [row for row in dataset[:int(0.85 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = [row for row in dataset[int(0.85 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classificator = GaussianNB()
    classificator.fit(train_x, train_y)
    predictions = classificator.predict(test_x)

    print(accuracy_score(test_y, predictions))
    print(classificator.predict([test_input])[0])
    print(classificator.predict_proba([test_input]))
