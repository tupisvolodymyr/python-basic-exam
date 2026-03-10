"""
Задача 2: Парсинг чисел з рядка

Реалізуйте функцію, використовуючи:
- типи даних
- змінні
- оператори
- умовні конструкції
- цикли
- базові методи рядків (split, strip)
"""


def parse_numbers(text: str) -> list[int]:
    my_list = []
    parts = text.split(",")
    for char in parts:
        delete_spaces = char.strip()
        if delete_spaces:
            number = int(delete_spaces)
            my_list.append(int(delete_spaces))
    return my_list



    """
    Потрібно перетворити рядок з числами, розділеними комами,
    у список цілих чисел.

    Вимоги:
    - Розділити рядок по комі.
    - Прибрати зайві пробіли навколо кожного елемента.
    - Ігнорувати пусті частини (наприклад між двома комами).
    - Перетворити кожне значення в int.
    - Якщо рядок пустий — повернути пустий список.

    ⚠️ Зверніть увагу:
    - Між комами можуть бути пробіли.
    - Можуть бути від’ємні числа.
    - Може бути кома на початку або в кінці рядка.

    Підказка:
    - Використайте split(",")
    - Далі пройдіться циклом по частинах
    - Для кожної частини використайте strip()
    - Перевірте, чи рядок не пустий перед перетворенням в int

    Приклади:
        parse_numbers("1,2,3") -> [1, 2, 3]
        parse_numbers("1, 2, 3") -> [1, 2, 3]
        parse_numbers("1,  , 3") -> [1, 3]
        parse_numbers("") -> []
    """



if __name__ == "__main__":
    print("\n" + "="*60)
    print("Testing Task 2: Parse Numbers")
    print("="*60 + "\n")
    
    # Test cases
    tests = [
        ("1,2,3", [1, 2, 3], "Basic comma-separated numbers"),
        ("1, 2, 3", [1, 2, 3], "With spaces after commas"),
        ("1,  2,   3", [1, 2, 3], "Multiple spaces"),
        ("1,  , 3", [1, 3], "Empty parts between commas"),
        ("", [], "Empty string"),
        ("42", [42], "Single number"),
        ("-1, -2, -3", [-1, -2, -3], "Negative numbers"),
        ("10, -5, 0, 15", [10, -5, 0, 15], "Mixed positive and negative"),
        ("0, 0, 0", [0, 0, 0], "Zero values"),
        ("1,2,3,", [1, 2, 3], "Trailing comma"),
        (",1,2,3", [1, 2, 3], "Leading comma"),
    ]
    
    passed = 0
    failed = 0
    
    for text, expected, description in tests:
        print(f"Running test: {description}")
        print(f"  Input: '{text}'")
        result = parse_numbers(text)
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        
        if result == expected:
            print(f"  ✓ PASS\n")
            passed += 1
        else:
            print(f"  ✗ FAIL\n")
            failed += 1
    
    print("="*60)
    print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests")
    print("="*60 + "\n")
    
    if failed == 0:
        print("🎉 Congratulations! All tests passed!\n")
    else:
        print("❌ Some tests failed. Please review your implementation.\n")
