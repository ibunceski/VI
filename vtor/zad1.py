import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from datasets.zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    test_input = list(input().split(" "))
    test_input_enc = encoder.transform([test_input])

    train_set = [row for row in dataset[:int(0.75 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_x_enc = encoder.transform(train_x)
    train_y = [row[-1] for row in train_set]

    test_set = [row for row in dataset[int(0.75 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_x_enc = encoder.transform(test_x)
    test_y = [row[-1] for row in test_set]

    classificator = CategoricalNB()
    classificator.fit(train_x_enc, train_y)

    predictions = classificator.predict(test_x_enc)

    print(accuracy_score(test_y, predictions))
    print(classificator.predict(test_input_enc)[0])
    print(classificator.predict_proba(test_input_enc))
