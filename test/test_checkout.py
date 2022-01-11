from typing import Union

import pytest

from checkout.core import Checkout, DiscountError
from pytest import approx

checkout = Union[Checkout, None]


def setup_module(module):
    global checkout
    checkout = Checkout()
    checkout.add_item("basketball", 24.99)
    checkout.add_item("basketball shoes", 79.99)


def test_can_calculate_total():
    assert checkout.total() == approx(24.99 + 79.99)


def test_can_discount_item():
    checkout.discount_item("basketball", 10)
    assert checkout.total() == approx(24.99 + 79.99 - 10)


def test_throws_when_discount_results_in_negative_total():
    with pytest.raises(DiscountError):
        checkout.discount_item("basketball shoes", 80)
