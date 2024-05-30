from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from datasets.zad12_dataset import dataset

if __name__ == "__main__":
    hidden_layer_sizes = int(input())
    learning_rate_init = float(input())
    col_to_remove = int(input())
    test_case = list(map(float, input().split(" ")))

    train_set = [row for row in dataset[:int(0.8 * len(dataset))]]
    test_set = [row for row in dataset[int(0.8 * len(dataset)):]]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = MLPClassifier(random_state=0, hidden_layer_sizes=hidden_layer_sizes,
                               learning_rate_init=learning_rate_init, activation="relu", max_iter=20)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)
    classifier.fit(scaler.transform(train_x), train_y)

    predictions1 = classifier.predict(scaler.transform(train_x))
    predictions2 = classifier.predict(scaler.transform(test_x))

    accuracy1 = 0
    for pred, real in zip(predictions1, train_y):
        if pred == real:
            accuracy1 += 1

    accuracy1 /= len(train_y)

    accuracy2 = 0
    for pred, real in zip(predictions2, test_y):
        if pred == real:
            accuracy2 += 1

    accuracy2 /= len(test_y)

    if accuracy1 > (accuracy2 * 1.15):
        print(f'Se sluchuva overfitting')
        train_x = [row[:col_to_remove] + row[col_to_remove + 1:] for row in train_x]
        scaler.fit(train_x)
        classifier.fit(scaler.transform(train_x), train_y)
        test_case = test_case[:col_to_remove] + test_case[col_to_remove + 1:]
        print(1 if classifier.predict([test_case])[0] == 0 else 0)
    else:
        print(f'Ne se sluchuva overfitting')
        print(classifier.predict([test_case])[0])

