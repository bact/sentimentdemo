# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""A preprocessing script for a text classification model."""

import sys

from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess, remove_dup_spaces


def preprocess_text(text: str) -> str:
    """Preprocess a text for a text classification model.

    :param text: The text to preprocess.
    :type text: str
    :return: Return the preprocessed text.
    :rtype: str
    """
    text = preprocess(text)
    text = " ".join(word_tokenize(text))
    text = remove_dup_spaces(text)
    return text


def main(data_dir_path: str, output_file_path: str) -> None:
    """Main function to preprocess a dataset for a text classification model.

    :param data_dir_path: Path to the directory containing the dataset.
    :type data_dir_path: str
    :param output_file_path: Path to the output file.
    :type output_file_path: str
    """
    labels = ["neg", "neu", "pos", "q"]

    with open(output_file_path, mode="w", encoding="utf-8") as destination:
        for label in labels:
            with open(
                f"{data_dir_path}/{label}.txt", mode="r", encoding="utf-8"
            ) as source:
                for line in source:
                    line = preprocess_text(line)
                    if len(line) > 0:
                        destination.write(f"__label__{label} {line}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python preprocess.py <data_dir_path> <output_file_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
