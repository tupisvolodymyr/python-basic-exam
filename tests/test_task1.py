"""
Tests for Task 1: Sum Until Negative
"""
import pytest
import sys
sys.path.insert(0, '../tasks')
from task1 import sum_until_negative


def test_basic_case():
    assert sum_until_negative([1, 2, 3, -1, 4]) == 6


def test_no_negative():
    assert sum_until_negative([5, 10, 15]) == 30


def test_negative_at_start():
    assert sum_until_negative([-5, 1, 2]) == 0


def test_empty_list():
    assert sum_until_negative([]) == 0


def test_single_positive():
    assert sum_until_negative([42]) == 42


def test_single_negative():
    assert sum_until_negative([-42]) == 0


def test_with_zero():
    assert sum_until_negative([0, 5, 10, -1]) == 15


def test_zero_only():
    assert sum_until_negative([0, 0, 0]) == 0


def test_negative_in_middle():
    assert sum_until_negative([10, 20, -5, 30, 40]) == 30
