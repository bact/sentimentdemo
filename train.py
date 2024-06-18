import fasttext


def main():
    model = fasttext.train_supervised("data/train.txt")
    model.quantize(input="data/train.txt", qnorm=True, retrain=True, cutoff=1000)
    model.save_model("model.bin")


if __name__ == "__main__":
    main()
