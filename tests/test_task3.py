"""
Tests for Task 3: Analyze Numbers
"""
import pytest
import sys
sys.path.insert(0, '../tasks')
from task3 import analyze_numbers


def test_basic_case():
    result = analyze_numbers([1, 2, 3, 4])
    assert result == {'count': 4, 'sum': 10, 'even': 2, 'odd': 2}


def test_empty_list():
    result = analyze_numbers([])
    assert result == {'count': 0, 'sum': 0, 'even': 0, 'odd': 0}


def test_all_even():
    result = analyze_numbers([2, 4, 6, 8])
    assert result == {'count': 4, 'sum': 20, 'even': 4, 'odd': 0}


def test_all_odd():
    result = analyze_numbers([1, 3, 5, 7])
    assert result == {'count': 4, 'sum': 16, 'even': 0, 'odd': 4}


def test_with_zero():
    result = analyze_numbers([0, 0, 0])
    assert result == {'count': 3, 'sum': 0, 'even': 3, 'odd': 0}


def test_negative_numbers():
    result = analyze_numbers([-2, -3, -4])
    assert result == {'count': 3, 'sum': -9, 'even': 2, 'odd': 1}


def test_mixed_numbers():
    result = analyze_numbers([10, -5, 0, 15, -2])
    assert result == {'count': 5, 'sum': 18, 'even': 2, 'odd': 3}


def test_single_number():
    result = analyze_numbers([7])
    assert result == {'count': 1, 'sum': 7, 'even': 0, 'odd': 1}


def test_large_numbers():
    result = analyze_numbers([100, 200, 300])
    assert result == {'count': 3, 'sum': 600, 'even': 3, 'odd': 0}
