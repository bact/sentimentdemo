# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""An evaluation script for a text classifcation model.

Output the F1 score, precision, and recall of a model on a test dataset.
"""

import sys

import fasttext
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder


def load_data(file_path: str) -> tuple[list, list]:
    """Load evaluation data from a file.

    :param file_path: Path to the evaluation data file.
    :type file_path: str
    :return: Return an evaluation dataset, as a tuple of labels and texts.
    :rtype: tuple[list, list]
    """

    labels = []
    texts = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            pair = line.strip().split(" ", 1)  # assumed one label per message

            if len(pair) == 2:
                labels.append(pair[0])
                texts.append(pair[1])

    return labels, texts


def main(model_file_path: str, test_data_file_path: str) -> None:
    """Main function to evaluate a model on a test dataset.

    :param model_file_path: _description_
    :type model_file_path: str
    :param test_data_file_path: _description_
    :type test_data_file_path: str
    """
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
    main(sys.argv[1], sys.argv[2])
