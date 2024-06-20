# SPDX-License-Identifier: CC0-1.0

import fasttext


def main():
    model = fasttext.train_supervised("train.txt")
    model.quantize(input="train.txt", qnorm=True, retrain=True, cutoff=256)
    model.save_model("model.bin")


if __name__ == "__main__":
    main()
