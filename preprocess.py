# SPDX-License-Identifier: CC0-1.0

import sys

from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess, remove_dup_spaces


def preprocess_text(text: str) -> str:
    text = preprocess(text)
    text = " ".join(word_tokenize(text))
    text = remove_dup_spaces(text)
    return text


def main(data_dir_path: str, output_file_path: str) -> None:
    labels = ["neg", "neu", "pos", "q"]

    with open(output_file_path, "w") as destination:
        for label in labels:
            with open(f"{data_dir_path}/{label}.txt", "r") as source:
                for line in source:
                    line = preprocess_text(line)
                    if len(line) > 0:
                        destination.write(f"__label__{label} {line}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python preprocess.py <data_dir_path> <output_file_path>")
        sys.exit(1)
    data_dir_path = sys.argv[1]
    output_file_path = sys.argv[2]
    main(data_dir_path, output_file_path)
