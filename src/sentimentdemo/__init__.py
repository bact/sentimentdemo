# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""Sentiment analysis demo."""

from .predict import predict
from .preprocess import preprocess_text as preprocess
from .train import train

__all__ = ["predict", "preprocess", "train"]
