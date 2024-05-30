import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import accuracy_score
from datasets.zad10_dataset import dataset

if __name__ == '__main__':

    warnings.filterwarnings('ignore', category=ConvergenceWarning)
    for row in dataset:
        if row[-1] >= 5:
            row[-1] = 1
        else:
            row[-1] = 0

    x = int(input()) / 100

    train_set = [row for row in dataset[int(x * len(dataset)):]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = [row for row in dataset[:int(x * len(dataset))]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = DecisionTreeClassifier(random_state=0, criterion="gini")
    classifier.fit(train_x, train_y)

    features_list = list(classifier.feature_importances_)

    least_important_col = features_list.index(min(features_list))

    train_x = [row[:least_important_col] + row[least_important_col + 1:] for row in train_x]
    test_x = [row[:least_important_col] + row[least_important_col + 1:] for row in test_x]

    MLclassifier = MLPClassifier(random_state=0, hidden_layer_sizes=15,activation="relu", learning_rate_init=0.001, max_iter=200)

    standard_scaler = StandardScaler()
    min_max_scaler = MinMaxScaler()

    MLclassifier.fit(standard_scaler.fit_transform(train_x), train_y)
    print(f'Tocnost so StandardScaler: {accuracy_score(test_y, MLclassifier.predict(standard_scaler.transform(test_x)))}')
    MLclassifier.fit(min_max_scaler.fit_transform(train_x), train_y)
    print(f'Tocnost so MinMaxScaler: {accuracy_score(test_y, MLclassifier.predict(min_max_scaler.transform(test_x)))}')