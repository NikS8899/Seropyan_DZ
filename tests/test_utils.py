# coding: Windows-1251

from src.utils import transactions


def test_transactions():
    assert transactions(path="") == []
