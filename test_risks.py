import pytest
from tracker import fee, summarize


def test_negative_amount_rejected():
    with pytest.raises(ValueError):
        summarize([{"amount": -50, "category": "x", "method": "card"}])


def test_unknown_method_rejected():
    with pytest.raises(ValueError):
        fee("crypto", 100)


def test_float_total_is_rounded():
    t, _ = summarize([{"amount": 0.1, "category": "x", "method": "cash"},
                      {"amount": 0.2, "category": "x", "method": "cash"}])
    assert t == 0.3
