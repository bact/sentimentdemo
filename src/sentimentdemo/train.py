# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""A training script for a text classification model."""

import sys
import time

import fasttext


def train(train_data_file_path: str, valid_data_file_path: str, model_file_path: str):
    """Train a text classification model.

    :param train_data_file_path: Path to the training data file.
    :type train_data_file_path: str
    :param valid_data_file_path: Path to the validation data file.
    :type valid_data_file_path: str
    :param model_file_path: Path to save the trained model.
    :type model_file_path: str
    """
    # Auto-tune hyperparameters.
    # Limit the duration to 2 hours. Limit the model size to 100K.
    model = fasttext.train_supervised(
        input=train_data_file_path,
        autotuneDuration=7200,
        autotuneModelSize="100K",
        autotuneValidationFile=valid_data_file_path,
    )

    # Print final hyperparameters
    if hasattr(model, "f"):
        print("Final hyperparameters:")
        args_obj = model.f.getArgs()
        for hparam in dir(args_obj):
            if not hparam.startswith("__"):
                print(f"{hparam}: {getattr(args_obj, hparam)}")

    model.save_model(model_file_path)


def main(train_data_file_path: str, valid_data_file_path: str, model_file_path: str):
    """_summary_

    :param train_data_file_path: Path to the training data file.
    :type train_data_file_path: str
    :param valid_data_file_path: Path to the validation data file.
    :type valid_data_file_path: str
    :param model_file_path: Path to save the trained model.
    :type model_file_path: str
    """
    start_time = time.time()
    print(f"Starts : {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(start_time))}")

    train(train_data_file_path, valid_data_file_path, model_file_path)

    end_time = time.time()
    print(f"Ends   : {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(end_time))}")
    elapsed_time = end_time - start_time
    print(f"Elapsed: {elapsed_time} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python train.py "
            "<train_data_filename> <validation_data_filename> <model_filename>"
        )
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
