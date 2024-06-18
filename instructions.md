# Instruction for use

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

## Train a new model

Prepare the `data/` directory with four text files: `neg.txt` for negative
examples, `neu.txt` for neutral examples, `pos.txt` for positive examples, and
`q.txt` for question examples. One line per example.

Then run this commmand:

```shell
python preprocess.py
```

The training data will be preprocessed and saved as `data/train.txt`.

Then run this command:

```shell
python train.py
```

The new model will be saved to `model.bin`.
