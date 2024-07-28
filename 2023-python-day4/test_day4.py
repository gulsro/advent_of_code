import pytest

from day4 import check_line

def test_no_winner():
    card = "Card 1: 1 2 3 4 | 5 6 7 8"
    assert check_line(card) == 0

def test_one_winner():
    card = "Card 1: 1 2 3 4 5 | 5 6 7 8"
    assert check_line(card) == 1

def test_three_matches():
    card = "Card 1: 1 2 3 4 5 | 5 3 7 2 3"
    assert check_line(card) == 4