# Data preparation

The dataset is obtained from the [Wisesight Sentiment Corpus][1], which is freely
available in the public domain and can be downloaded without registration.

Special characters, including repeated characters, were removed.
Phone numbers, email addresses, and URLs were replaced with a specific symbol.
This preprocessing is done by [th-simple-preprocessor][2].

The text will then be tokenized into words using a dictionary-based
[newmm-tokenizer][3].

For example, this is a text before preprocessing and tokenization:

```text
จัดไป 55555 ตอนนี้พร้อม เอาหลานมาด้วย
```

This is the same text after processing and tokenization:

```text
จัด ไป wshaha ตอนนี้ พร้อม เอา หลาน มา ด้วย
```

(Notes: `55555` is a laughter expression, which is based on a number `5` --
pronounced "ha" in Thai. It is replaced by a `wshaha` token.)

Then a label will be applied at the beginning of the line, to match the format
that is expected by [fastText][4]:

```text
__label__neu จัด ไป wshaha ตอนนี้ พร้อม เอา หลาน มา ด้วย
```

100 samples are randomly selected to be included in the training set.

[1]: https://github.com/PyThaiNLP/wisesight-sentiment/
[2]: https://pypi.org/project/th-simple-preprocessor/
[3]: https://pypi.org/project/newmm-tokenizer/
[4]: https://fasttext.cc/
