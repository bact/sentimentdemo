# SPDX-License-Identifier: CC0-1.0

import sys
import time

import fasttext
from pyJoules.energy_meter import measure_energy


@measure_energy
def train(train_data_file_path: str, valid_data_file_path: str, model_file_path: str):
    # model = fasttext.train_supervised(
    #    input=train_data_file_path,
    #    autotuneValidationFile=valid_data_file_path,
    #    autotuneDuration=7200,  # 2 hours
    #    autotuneModelSize="500K",
    # )

    model = fasttext.train_supervised(
        input=train_data_file_path,
        lr=0.34,
        lrUpdateRate=100,
        epoch=100,
        dim=26,
        ws=5,
        wordNgrams=3,
        minCount=1,
        minCountLabel=0,
        minn=2,
        maxn=6,
        neg=5,
        loss="softmax",
        bucket=3036115,
        thread=3,
        t=0.0001,
        seed=0,
    )
    model = model.quantize(
        input=train_data_file_path,
        qnorm=True,
        retrain=True,
        cutoff=19700,
        qout=False,
        dsub=2,
    )

    # Print final hyperparameters
    # args_obj = model.f.getArgs()
    # for hparam in dir(args_obj):
    #    if not hparam.startswith("__"):
    #        print(f"{hparam}: {getattr(args_obj, hparam)}")

    # model.save_model(model_file_path)


def main(train_data_file_path: str, valid_data_file_path: str, model_file_path: str):
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
            "Usage: python train.py <train_data_filename> <validation_data_filename> <model_filename>"
        )
        sys.exit(1)
    train_data_file_path = sys.argv[1]
    valid_data_file_path = sys.argv[2]
    model_file_path = sys.argv[3]
    main(train_data_file_path, valid_data_file_path, model_file_path)
