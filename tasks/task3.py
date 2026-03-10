"""
Задача 3: Аналіз списку чисел

Реалізуйте функцію, використовуючи тільки:
- типи даних
- змінні
- оператори
- умовні конструкції
- цикли
- функції
"""
from itertools import count


def analyze_numbers(numbers: list[int]) -> dict:
    my_dict = {"count": 0,
    "sum": 0,
    "even" : 0,
    "odd" : 0}
    if len(numbers):
        my_dict["count"] = len(numbers)
        my_dict["sum"] = sum(numbers)
    for number in numbers:
        if number % 2 == 0:
            my_dict["even"] += 1
        elif number % 2 == 1:
            my_dict["odd"] += 1
    return my_dict





    """
    Потрібно проаналізувати список чисел і повернути словник зі статистикою.

    Функція повинна повернути словник з такими ключами:
    - 'count' — загальна кількість елементів
    - 'sum' — сума всіх чисел
    - 'even' — кількість парних чисел
    - 'odd' — кількість непарних чисел

    ⚠️ Важливо:
    - Якщо список пустий — всі значення повинні бути 0.
    - 0 вважається парним числом.
    - Використовуйте оператор % для визначення парності.

    Підказка:
    - Створіть змінні-лічильники.
    - Пройдіться циклом по списку.
    - Оновлюйте лічильники всередині циклу.
    - В кінці сформуйте словник з результатами.

    Приклади:
        analyze_numbers([1, 2, 3, 4])
        -> {'count': 4, 'sum': 10, 'even': 2, 'odd': 2}

        analyze_numbers([])
        -> {'count': 0, 'sum': 0, 'even': 0, 'odd': 0}

        analyze_numbers([0, 0, 0])
        -> {'count': 3, 'sum': 0, 'even': 3, 'odd': 0}
    """
    pass


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Testing Task 3: Analyze Numbers")
    print("="*60 + "\n")
    
    # Test cases
    tests = [
        ([1, 2, 3, 4], {'count': 4, 'sum': 10, 'even': 2, 'odd': 2}, "Basic mixed numbers"),
        ([], {'count': 0, 'sum': 0, 'even': 0, 'odd': 0}, "Empty list"),
        ([2, 4, 6, 8], {'count': 4, 'sum': 20, 'even': 4, 'odd': 0}, "All even numbers"),
        ([1, 3, 5, 7], {'count': 4, 'sum': 16, 'even': 0, 'odd': 4}, "All odd numbers"),
        ([0, 0, 0], {'count': 3, 'sum': 0, 'even': 3, 'odd': 0}, "Only zeros"),
        ([-2, -3, -4], {'count': 3, 'sum': -9, 'even': 2, 'odd': 1}, "Negative numbers"),
        ([10, -5, 0, 15, -2], {'count': 5, 'sum': 18, 'even': 2, 'odd': 3}, "Mixed positive and negative"),
        ([7], {'count': 1, 'sum': 7, 'even': 0, 'odd': 1}, "Single number"),
        ([100, 200, 300], {'count': 3, 'sum': 600, 'even': 3, 'odd': 0}, "Large numbers"),
    ]
    
    passed = 0
    failed = 0
    
    for numbers, expected, description in tests:
        print(f"Running test: {description}")
        print(f"  Input: {numbers}")
        result = analyze_numbers(numbers)
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
