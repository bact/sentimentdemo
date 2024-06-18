import sys

import fasttext
from newmm_tokenizer.tokenizer import word_tokenize
from th_preprocessor.preprocess import preprocess

model = fasttext.load_model("model.bin")


def main():
    if len(sys.argv) != 2:
        print("Usage: python predict.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    text = preprocess(text)
    text = " ".join(word_tokenize(text))
    text = preprocess(text)
    labels, probabilities = model.predict(text)
    print(f"Label: {labels[0]}, Probability: {probabilities[0]}")


if __name__ == "__main__":
    main()
