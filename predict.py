# SPDX-License-Identifier: CC0-1.0

import sys
import time

import fasttext
from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess, remove_dup_spaces, remove_stopwords

model = fasttext.load_model("model.bin")


def predict(text: str):
    text = preprocess(text)
    text = " ".join(remove_stopwords(word_tokenize(text)))
    text = remove_dup_spaces(text)

    labels, probabilities = model.predict(text)
    print(f"Label: {labels[0][9:]}, Probability: {probabilities[0]:.4f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py \"<text>\"")
        sys.exit(1)

    text = sys.argv[1]
    predict(text)
