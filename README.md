# sentimentdemo

A simple text classification application, published solely as an artifact for
the purpose of demonstrating
[a software bill of materials (SBOM)](https://en.wikipedia.org/wiki/Software_supply_chain).

*Not suitable for any serious use of text classification.*

The main content of this repository is the software bill of materials at
[bom.spdx3.json](./bom.spdx3.json).
Other files are given to complete the illustration.

Design goals:

- Small enough for human comprehension
- Elaborate enough to demonstrate the use of different information fields

Will eventually be submitted to
[spdx/spdx-examples](https://github.com/spdx/spdx-examples) repo.

## Content

```text
├── LICENSE               License information
├── README.md             This README file
├── bom.spdx3.json        Software bill of materials, in SPDX 3 format
├── data                  Dataset, preprocessed and tokenized
│   ├── test.txt          Testing data
│   ├── train.txt         Training data
│   └── valid.txt         Validation data
├── evaluate.py           A script to evaluate prediction performance
├── model.bin             A sentiment analysis model
├── predict.py            A script to predict a label of a text
├── preprocess.py         A script to prepare training data
├── rawdata               Raw dataset, before preprocessing
│   ├── test              Testing data
│   │   ├── neg.txt       Testing samples for label "neg" (negative)
│   │   ├── neu.txt       Testing samples for label "neu" (neutral)
│   │   ├── pos.txt       Testing samples for label "pos" (positive)
│   │   └── q.txt         Testing samples for label "q" (question)
│   ├── train             Training data
│   │   └── ...
│   └── valid             Validation data
│       └── ...
├── requirements.txt      List of required Python libraries
├── techdocs              Technical documentation
│   ├── dataprepare.md    Data prepration
│   └── instructions.md   Instruction for use
└── train.py              A script to build a model
```

## Usage

See [instruction for use](./techdocs/instructions.md) for how to use the
application.

## Data preparation

See [data preparation](./techdocs/dataprepare.md).

## Notes

- The energy used by the computer during model training is tracked by
  [energy-tracker](https://github.com/rdegges/energy-tracker).
  It measures how much energy the computer uses during the training.
  This means the actual energy used for training the model might be a bit less
  than the reported amount.

## Licenses

Apart from the data and components listed in the table below, the code and
content in this repository are dedicated to the public domain under the terms
of Creative Commons Zero ("CC0") 1.0 Universal, which have no copyright and
related or neighboring rights worldwide to the extent allowed by law.

| Component | Name | License | Notes |
| --------- | ---- | ------- | ----- |
| Training data | [Wisesight Sentiment Corpus](https://github.com/PyThaiNLP/wisesight-sentiment) | Creative Commons Zero v1.0 Universal | In `data/`. For the interest of size, the excerpt contains only 100 lines. See [data preparation](./techdocs/dataprepare.md). |
| Text preprocessor | [th-simple-preprocessor](https://pypi.org/project/th-simple-preprocessor/) |  Apache License 2.0 | |
| Word tokenizer | [newmm-tokenizer](https://pypi.org/project/newmm-tokenizer/) | Apache License 2.0 | Inherited the license from [PyThaiNLP](https://pypi.org/project/pythainlp/). |
| Text classifier | [fastText](https://pypi.org/project/fasttext/) | MIT License | |
| Array package | [NumPy](https://pypi.org/project/numpy/) | BSD License | |

The specific version information can be found in
[requirements.txt](./requirements.txt).
