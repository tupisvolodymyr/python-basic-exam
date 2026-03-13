import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from task_02_passed_students import build_passed_students_map


def test_build_passed_students_map_basic():
    records = [
        {"name": " Alice ", "score": 75},
        {"name": "Bob", "score": 50},
        {"name": " Clara ", "score": 90}
    ]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {"Alice": 75, "Clara": 90}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_empty_list():
    records = []
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_all_passed():
    records = [
        {"name": "Alice", "score": 60},
        {"name": "Bob", "score": 70},
        {"name": "Clara", "score": 80}
    ]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {"Alice": 60, "Bob": 70, "Clara": 80}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_all_failed():
    records = [
        {"name": "Alice", "score": 50},
        {"name": "Bob", "score": 30},
        {"name": "Clara", "score": 59}
    ]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_boundary_score():
    records = [
        {"name": "Alice", "score": 60},
        {"name": "Bob", "score": 59}
    ]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {"Alice": 60}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_high_scores():
    records = [
        {"name": " John ", "score": 95},
        {"name": " Jane ", "score": 100}
    ]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {"John": 95, "Jane": 100}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected


def test_build_passed_students_map_single_student():
    records = [{"name": " Test ", "score": 85}]
    print(f"\nInput: {records}")
    result = build_passed_students_map(records)
    expected = {"Test": 85}
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    assert result == expected
