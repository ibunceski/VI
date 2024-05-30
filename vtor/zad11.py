from datasets.zad11_dataset import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score

if __name__ == "__main__":
    x = int(input())
    classificator_type = input()
    col_to_remove = int(input())

    train_set = [row for row in dataset[x:]]
    test_set = [row for row in dataset[:x]]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier1 = DecisionTreeClassifier(random_state=0)
    classifier2 = DecisionTreeClassifier(random_state=0)

    if classificator_type == "NB":
        classifier1 = GaussianNB()
        classifier2 = GaussianNB()
    elif classificator_type == "NN":
        classifier1 = MLPClassifier(random_state=0, hidden_layer_sizes=3, activation="relu", learning_rate_init=0.003,
                                    max_iter=200)
        classifier2 = MLPClassifier(random_state=0, hidden_layer_sizes=3, activation="relu", learning_rate_init=0.003,
                                    max_iter=200)

    classifier1.fit(train_x, train_y)
    predictions1 = classifier1.predict(test_x)
    accuracy1 = 0

    for pred, real in zip(predictions1, test_y):
        if pred == real:
            accuracy1 += 1

    accuracy1 /= len(test_y)

    train_x = [row[:col_to_remove] + row[col_to_remove + 1:] for row in train_x]
    test_x = [row[:col_to_remove] + row[col_to_remove + 1:] for row in test_x]

    classifier2.fit(train_x, train_y)
    predictions2 = classifier2.predict(test_x)
    accuracy2 = 0

    for pred, real in zip(predictions2, test_y):
        if pred == real:
            accuracy2 += 1

    accuracy2 /= len(test_y)

    predicitions = predictions1
    tp, fp = 0, 0
    # print(f'accuracy1: {accuracy1} accuracy2: {accuracy2}')
    if accuracy1 > accuracy2:
        print(f'Klasifiktorot so site koloni ima pogolema tochnost')
    elif accuracy2 > accuracy1:
        print(f'Klasifiktorot so edna kolona pomalku ima pogolema tochnost')
        predicitions = predictions2
    else:
        print(f'Klasifikatorite imaat ista tochnost')

    for pred, real in zip(predicitions, test_y):
        if pred == 1 and real == 1:
            tp += 1
        elif pred == 1 and real == 0:
            fp += 1

    precision = 0.0 if tp + fp == 0 else tp / (tp + fp)
    print(precision)
