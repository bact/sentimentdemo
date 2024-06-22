# Instruction for use

This application is designed to predict the sentiment of text.

It was trained on Thai microblogging social media data and may have limitations
in predicting text from other genres or languages.

## Prerequisites

Install the required dependencies.

- `fasttext==0.9.3` - For text classification model training and prediction.
- `newmm-tokenizer==0.2.2` - For Thai text tokenization.
- `numpy==1.26.4` - For all multidimensional arrays computations. Note that NumPy version 2 and later will not work.
- `th-simple-preprocessor==0.10.1` - For Thai text preprocessing.

```shell
pip install -r requirements.txt
```

## Predict a label of a text

```shell
python predict.py <text>
```

The script will print the predicted label for the provided text.

Possible labels are:

- `neg` - negative
- `neu` - neutral
- `pos` - positive
- `q` - question

```shell
$ python predict.py กินข้าวกัน
Label: pos, Probability: 0.2620
```

## Train a new model

Prepare the `data/` directory with four text files: `neg.txt` for negative
examples, `neu.txt` for neutral examples, `pos.txt` for positive examples, and
`q.txt` for question examples. One line per example.

Then run this commmand:

```shell
python preprocess.py data/train/ train.txt
```

The training data in `data/train/` directory will be
[preprocessed](./dataprepare.md) and saved as `train.txt`.

Then run this command:

```shell
python train.py
```

The new model will be saved to `model.bin`.
