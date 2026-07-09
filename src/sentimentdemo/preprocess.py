# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: CC0-1.0

"""
Provides text preprocessing function.
"""

import sys

from newmm_tokenizer.tokenizer import word_tokenize
from pitloom import loom
from th_preprocessor.preprocess import preprocess, remove_dup_spaces

LABELS = ["neg", "neu", "pos", "q"]
SPLITS = ["train", "valid", "test"]


def preprocess_text(text: str) -> str:
    """
    Preprocesses a given text string by applying tokenization, removing
    duplicate spaces, and other preprocessing steps.

    Args:
        text (str): The input text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    text = preprocess(text)
    text = " ".join(word_tokenize(text))
    text = remove_dup_spaces(text)
    return text


def main(rawdata_dir: str, processed_dir: str) -> None:
    """
    Preprocess every dataset split (train/valid/test) found under
    *rawdata_dir* into fastText-formatted files under *processed_dir*.

    All splits are recorded in a single accumulating loom run rather than
    three separate ones, so the resulting SBOM fragment traces every split's
    dataset lineage -- more ergonomic than requiring a developer to declare
    three separate provenance contexts, and it avoids each split's run
    overwriting a shared fragment file.

    Args:
        rawdata_dir (str): Directory containing one subdirectory per split
            (e.g. ``rawdata/train``, ``rawdata/valid``, ``rawdata/test``),
            each with per-label text files.
        processed_dir (str): Directory to write each split's
            fastText-formatted output file to (e.g. ``data/train.txt``).
    """
    with loom.run("fragments/preprocess.spdx3.json", pretty=True) as run:
        for split in SPLITS:
            data_dir = f"{rawdata_dir}/{split}"
            output_path = f"{processed_dir}/{split}.txt"

            input_names = [f"{data_dir}/{label}.txt" for label in LABELS]
            for name in input_names:
                run.add_input_dataset(name, dataset_type="text")

            run.add_output_dataset(
                output_path,
                dataset_type="text",
                data_preprocessing=[
                    "thai-text-normalization",
                    "newmm-word-tokenization",
                    "fasttext-label-format",
                ],
                # Scope this split's hasInput lineage to only its own label
                # files -- without this, every output in the run would link
                # back to every input the run has seen, cross-contaminating
                # the train/valid/test splits' lineage.
                input_datasets=input_names,
            )

            with open(output_path, mode="w", encoding="utf-8") as destination:
                for label in LABELS:
                    with open(
                        f"{data_dir}/{label}.txt", mode="r", encoding="utf-8"
                    ) as source:
                        for line in source:
                            line = preprocess_text(line)
                            if len(line) > 0:
                                destination.write(f"__label__{label} {line}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python preprocess.py <rawdata_dir> <processed_dir>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
