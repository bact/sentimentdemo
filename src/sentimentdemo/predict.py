# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: CC0-1.0

"""
Predicts the label of a given text.

The text is preprocessed before prediction, including tokenization,
stopword removal, and space normalization.
"""

import os
import sys
from typing import Any, cast

import fasttext
from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess as th_preprocess
from th_preprocessor.preprocess import remove_dup_spaces, remove_stopwords

_MODEL: Any = None


def predict(text: str) -> tuple[list[str], list[float]]:
    """
    Predict the label of the given text using the loaded fastText model.

    Args:
        text (str): The input text to be classified.

    Returns:
        tuple: A tuple containing two lists:
        - list of str: The predicted labels.
        - list of float: The probabilities associated with each label.
    """
    global _MODEL  # pylint: disable=global-statement
    if _MODEL is None:
        model_path = os.path.join(os.path.dirname(__file__), "model.bin")
        _MODEL = fasttext.load_model(model_path)

    text = th_preprocess(text)
    text = " ".join(remove_stopwords(word_tokenize(text)))
    text = remove_dup_spaces(text)

    # fastText usually returns a tuple of strings and a numpy array
    return cast(tuple[list[str], list[float]], _MODEL.predict(text))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python predict.py "<text>"')
        sys.exit(1)

    labels, probabilities = predict(sys.argv[1])
    print(f"Label: {labels[0][9:]}, Probability: {probabilities[0]:.4f}")
