"""
Tests for Task 2: Parse Numbers
"""
import pytest
import sys
sys.path.insert(0, '../tasks')
from task2 import parse_numbers


def test_basic_case():
    assert parse_numbers("1,2,3") == [1, 2, 3]


def test_with_spaces():
    assert parse_numbers("1, 2, 3") == [1, 2, 3]


def test_multiple_spaces():
    assert parse_numbers("1,  2,   3") == [1, 2, 3]


def test_empty_parts():
    assert parse_numbers("1,  , 3") == [1, 3]


def test_empty_string():
    assert parse_numbers("") == []


def test_single_number():
    assert parse_numbers("42") == [42]


def test_negative_numbers():
    assert parse_numbers("-1, -2, -3") == [-1, -2, -3]


def test_mixed_numbers():
    assert parse_numbers("10, -5, 0, 15") == [10, -5, 0, 15]


def test_zero_values():
    assert parse_numbers("0, 0, 0") == [0, 0, 0]


def test_trailing_comma():
    assert parse_numbers("1,2,3,") == [1, 2, 3]


def test_leading_comma():
    assert parse_numbers(",1,2,3") == [1, 2, 3]
