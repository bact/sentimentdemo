# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: CC0-1.0

"""
Trains a text classification model using supervised learning (fastText).
"""

import sys
import time

import fasttext
from pitloom import loom


def train(
    train_data_file_path: str, valid_data_file_path: str, model_file_path: str
) -> None:
    """
    Trains a fastText model with auto-tuned hyperparameters
    and saves the model to a file.

    Args:
        train_data_file_path (str): Path to the training data file.
        valid_data_file_path (str): Path to the validation data file.
        model_file_path (str): Path to save the trained model.

    Returns:
        None
    """
    with loom.shoot("fragments/train.spdx3.json", pretty=True) as shot:
        shot.set_model(model_file_path, model_type="supervised")
        shot.add_dataset(train_data_file_path, dataset_type="text")
        shot.add_validation_dataset(valid_data_file_path, dataset_type="text")

        # Auto-tune hyperparameters.
        # Limit the duration to 2 hours. Limit the model size to 100K.
        model = fasttext.train_supervised(
            input=train_data_file_path,
            autotuneDuration=7200,
            autotuneModelSize="100K",
            autotuneValidationFile=valid_data_file_path,
        )

        # Capture and record final hyperparameters in SBOM fragment
        if hasattr(model, "f"):
            args_obj = model.f.getArgs()
            hparams = {
                h: str(getattr(args_obj, h))
                for h in dir(args_obj)
                if not h.startswith("__")
            }
            shot.set_model_hyperparameters(hparams)

            print("Final hyperparameters:")
            for k, v in hparams.items():
                print(f"{k}: {v}")

        model.save_model(model_file_path)


def main(train_data_path: str, valid_data_path: str, model_path: str) -> None:
    """
    Main function to handle the training process and print start and end times.

    Args:
        train_data_path (str): Path to the training data file.
        valid_data_path (str): Path to the validation data file.
        model_path (str): Path to save the trained model.

    Returns:
        None
    """
    start_time = time.time()
    print(f"Starts : {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(start_time))}")

    train(train_data_path, valid_data_path, model_path)

    end_time = time.time()
    print(f"Ends   : {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(end_time))}")
    elapsed_time = end_time - start_time
    print(f"Elapsed: {elapsed_time} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python train.py <train_file> <validation_file> <model_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
