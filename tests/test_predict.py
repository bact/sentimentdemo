# SPDX-FileCopyrightText: 2024-present Arthit Suriyawongkul <suriyawa@tcd.ie>
#
# SPDX-License-Identifier: CC0-1.0

"""Test package for sentimentdemo."""

from sentimentdemo.predict import predict
from sentimentdemo.preprocess import preprocess_text


def test_predict():
    """Test predict function."""
    text = "This is a test ."
    labels, _ = predict(text)
    assert labels[0] in [
        "__label__neg",
        "__label__neu",
        "__label__pos",
        "__label__q",
    ]


def test_preprocess_text():
    """Test preprocess_text function."""
    text = "test"
    preprocessed_text = preprocess_text(text)
    assert isinstance(preprocessed_text, str)
