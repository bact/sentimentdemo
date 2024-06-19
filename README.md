# sentimentdemo

A simple text classification application, published mainly as an artifact for
the purpose of demonstrating a software bill of materials.

*Not suitable for any serious use.*

## Content

The main content of this repository is the software bill of materials at
[sbom.spdx3.json](./sbom.spdx3.json).
Other files are given to complete the illustration.

```text
├── LICENSE               License information
├── README.md             This README file
├── data                  Data before preprocessed
│   ├── neg.txt           Samples for label "neg" (negative)
│   ├── neu.txt           Samples for label "neu" (neutral)
│   ├── pos.txt           Samples for label "pos" (positive)
│   └── q.txt             Samples for label "q" (question)
├── bom.spdx3.json        Software bill of materials, in SPDX 3 format
├── model.bin             A sentiment analysis model
├── predict.py            A script to predict a label of a text
├── preprocess.py         A script to prepare training data
├── requirements.txt      List of required Python libraries
├── techdocs              Technical documentation
│   ├── dataprepare.md    Data prepration
│   └── instructions.md   Instruction for use
├── train.py              A script to build a model
└── train.txt             Training data (label, tokenized text)
```

## Usage

See [instruction for use](./techdocs/instructions.md) for how to use the
application.

## Data preparation

See [data preparation](./techdocs/dataprepare.md).

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
