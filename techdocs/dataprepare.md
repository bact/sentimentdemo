# Data preparation

## Original dataset

The Thai social media sentiment dataset is obtained from the
[Wisesight Sentiment Corpus][1], which is freely available in the public domain
and can be downloaded without registration.

The dataset consists of four files, each corresponding to a specific sentiment
label: positive, neutral, negative, and question. Each file contains social
media messages for that sentiment label, with one message per line.

The original dataset has already undergone some level of anonymization, with
personal identifiable information removed or masked.

## Preparation of training data

From each file, 100 samples are randomly selected. This results in a total of
400 samples across the four labels.

Messages undergo the following normlaization treatments:

- Hashtags and special characters are removed.
- Accented characters are normalized.
- Thai vowel variations are normalized.
- Thai digits are converted to Arabic digits.
- @Mentions, URLs, filenames, phone numbers, long numbers, and laughter
  expressions are replaced with placeholders indicating their category
- Emojis are preserved.

This preprocessing is performed by [th-simple-preprocessor library][2].

The text is then tokenized into words using a dictionary-based tokenizer,
[newmm-tokenizer][3].

Example:

Before preprocessing and tokenization:

```text
จัดไป 55555 ตอนนี้พร้อม เอาหลานมาด้วย
```

After preprocessing and tokenization:

```text
จัด ไป WSHAHA ตอนนี้ พร้อม เอา หลาน มา ด้วย
```

(Note: In Thai, the sequence of fives (55555) is a common laughter expression
where each "5" is pronounced as "ha." During preprocessing, this laughter
expression is replaced with the token `WSHAHA`.)

A sentiment label is then added at the beginning of each line, following the
format expected by [fastText][4]:

```text
__label__neu จัด ไป WSHAHA ตอนนี้ พร้อม เอา หลาน มา ด้วย
```

[1]: https://github.com/PyThaiNLP/wisesight-sentiment/
[2]: https://pypi.org/project/th-simple-preprocessor/
[3]: https://pypi.org/project/newmm-tokenizer/
[4]: https://fasttext.cc/
