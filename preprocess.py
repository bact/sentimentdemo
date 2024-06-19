# SPDX-License-Identifier: CC0-1.0

from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess


def get_training_lines(file_path, label):
    training_lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = preprocess(line)
            line = " ".join(word_tokenize(line))
            line = preprocess(line)
            training_lines.append(f"__label__{label} {line}")
    return training_lines


def main():
    training_data = []
    training_data += get_training_lines("data/neg.txt", "neg")
    training_data += get_training_lines("data/neu.txt", "neu")
    training_data += get_training_lines("data/pos.txt", "pos")
    training_data += get_training_lines("data/q.txt", "q")

    with open("train.txt", "w") as file:
        for line in training_data:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
