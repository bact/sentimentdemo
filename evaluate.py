import sys

import fasttext
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder


def load_data(file_path: str) -> tuple[list, list]:
    labels = []
    texts = []
    with open(file_path, "r") as file:
        for line in file:
            pair = line.strip().split(" ", 1)  # assumed one label per message

            if len(pair) == 2:
                labels.append(pair[0])
                texts.append(pair[1])

    return labels, texts


def main(model_file_path: str, test_data_file_path: str) -> None:
    labels, data = load_data(test_data_file_path)
    model = fasttext.load_model(model_file_path)

    predictions = [model.predict(x)[0][0] for x in data]

    le = LabelEncoder()
    numeric_labels = le.fit_transform(labels)
    numeric_predictions = le.transform(predictions)

    f1 = f1_score(numeric_labels, numeric_predictions, average="weighted")
    precision = precision_score(numeric_labels, numeric_predictions, average="weighted")
    recall = recall_score(numeric_labels, numeric_predictions, average="weighted")

    print(f"F1 Score: {f1}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evaluate.py <model_file_path> <test_data_file_path>")
        sys.exit(1)
    model_file_path = sys.argv[1]
    test_data_file_path = sys.argv[2]
    main(model_file_path, test_data_file_path)
