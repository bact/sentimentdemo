# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""A prediction script for a text classifcation model."""

import sys

import fasttext
from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess, remove_dup_spaces, remove_stopwords

model = fasttext.load_model("model.bin")


def predict(text: str) -> tuple[list, list]:
    """Predict the sentiment of a text.

    :param text: The text to predict the sentiment of.
    :type text: str
    :return: Return a tuple of labels and probabilities.
    :rtype: tuple[list, list]
    """
    text = preprocess(text)
    text = " ".join(remove_stopwords(word_tokenize(text)))
    text = remove_dup_spaces(text)

    return model.predict(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python predict.py "<text>"')
        sys.exit(1)

    labels, probabilities = predict(sys.argv[1])
    print(f"Label: {labels[0][9:]}, Probability: {probabilities[0]:.4f}")
