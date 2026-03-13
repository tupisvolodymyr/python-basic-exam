import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from task_03_flatten_even_numbers import flatten_even_numbers


def test_flatten_even_numbers_basic():
    matrix = [[1, 2, 3], [4, 5], [6]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [2, 4, 6]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_empty_matrix():
    matrix = []
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = []
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_empty_rows():
    matrix = [[], [], []]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = []
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_all_even():
    matrix = [[2, 4], [6, 8], [10]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [2, 4, 6, 8, 10]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_all_odd():
    matrix = [[1, 3], [5, 7], [9]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = []
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_single_row():
    matrix = [[1, 2, 3, 4, 5, 6]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [2, 4, 6]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_single_element():
    matrix = [[2]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [2]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_with_zero():
    matrix = [[0, 1, 2], [3, 4]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [0, 2, 4]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_flatten_even_numbers_negative():
    matrix = [[-2, -1], [0, 1], [2]]
    print(f"\nInput: {matrix}")
    result = flatten_even_numbers(matrix)
    expected = [-2, 0, 2]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected
