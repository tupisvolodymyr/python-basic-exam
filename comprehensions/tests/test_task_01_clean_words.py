import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from task_01_clean_words import clean_words


def test_clean_words_basic():
    words = [" Hello ", "WORLD", "   ", " Python "]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = ["hello", "world", "python"]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_empty_list():
    words = []
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = []
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_all_empty_strings():
    words = ["   ", "", "  ", "\t"]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = []
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_mixed_case():
    words = ["HeLLo", "WoRLd", "PyThOn"]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = ["hello", "world", "python"]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_no_spaces():
    words = ["hello", "world"]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = ["hello", "world"]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_only_spaces():
    words = ["  hello  ", "  world  "]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = ["hello", "world"]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_clean_words_single_word():
    words = [" Test "]
    print(f"\nInput: {words}")
    result = clean_words(words)
    expected = ["test"]
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected
