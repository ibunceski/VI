from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from datasets.zad13_dataset import dataset

if __name__ == "__main__":
    x1 = float(input())
    x2 = float(input())

    dataset0 = [row for row in dataset if row[-1] == 0]
    dataset1 = [row for row in dataset if row[-1] == 1]
    dataset2 = [row for row in dataset if row[-1] == 2]

    test_set = [row for row in dataset0[int(x2 * len(dataset0)):]] \
               + [row for row in dataset1[int(x2 * len(dataset1)):]] \
               + [row for row in dataset2[int(x2 * len(dataset2)):]]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier1 = GaussianNB()
    train_set_1 = [row for row in dataset0[:int(x1 * len(dataset0))]] \
                  + [row for row in dataset1[:int(x1 * len(dataset1))]] \
                  + [row for row in dataset2[:int(x1 * len(dataset2))]]

    train_x = [row[:-1] for row in train_set_1]
    train_y = [row[-1] for row in train_set_1]

    classifier1.fit(train_x, train_y)
    predictions1 = classifier1.predict(test_x)

    classifier2 = DecisionTreeClassifier()
    train_set_2 = [row for row in dataset0[int(x1 * len(dataset0)):(int(x2 * len(dataset0)))]] \
                  + [row for row in dataset1[int(x1 * len(dataset1)):(int(x2 * len(dataset1)))]] \
                  + [row for row in dataset2[int(x1 * len(dataset2)):(int(x2 * len(dataset2)))]]

    train_x = [row[:-1] for row in train_set_2]
    train_y = [row[-1] for row in train_set_2]

    classifier2.fit(train_x, train_y)
    predictions2 = classifier2.predict(test_x)

    classifier3 = RandomForestClassifier(n_estimators=3)
    train_set_3 = [row for row in dataset0[:int(x2 * len(dataset0))]] \
                  + [row for row in dataset1[:int(x2 * len(dataset1))]] \
                  + [row for row in dataset2[:int(x2 * len(dataset2))]]

    train_x = [row[:-1] for row in train_set_3]
    train_y = [row[-1] for row in train_set_3]

    classifier3.fit(train_x, train_y)
    predictions3 = classifier3.predict(test_x)

    accurate = 0
    for pred1, pred2, pred3, gt in zip(predictions1, predictions2, predictions3, test_y):
        right = 0
        if pred1 == gt:
            right += 1
        if pred2 == gt:
            right += 1
        if pred3 == gt:
            right += 1

        if right >= 2:
            accurate += 1

    accuracy = accurate / len(test_y)

    print(f'Tochnost: {accuracy}')
