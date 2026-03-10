"""
Задача 1: Сума до першого від’ємного

Реалізуйте функцію, використовуючи тільки базові можливості Python:
- типи даних
- змінні
- оператори
- умовні конструкції (if/elif/else)
- цикли (for або while)
- функції
"""


def sum_until_negative(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        if number < 0:
            break
        total += number
    return total





    """
    Потрібно порахувати суму чисел у списку ДО першого від’ємного числа.

    ⚠️ Важливо:
    - Як тільки зустрічається від’ємне число — потрібно зупинитися.
    - Саме від’ємне число НЕ входить у суму.
    - Якщо перший елемент від’ємний — результат має бути 0.
    - Якщо список пустий — результат має бути 0.

    Підказка:
    - Вам знадобиться змінна-накопичувач (наприклад total).
    - Подумайте, де саме потрібно перевіряти умову number < 0.
    - Чи потрібно використовувати break?

    Приклади:
        sum_until_negative([1, 2, 3, -1, 4]) -> 6
        sum_until_negative([5, 10, 15]) -> 30
        sum_until_negative([-5, 1, 2]) -> 0
        sum_until_negative([]) -> 0
    """


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Testing Task 1: Sum Until Negative")
    print("="*60 + "\n")
    
    # Test cases
    tests = [
        ([1, 2, 3, -1, 4], 6, "Basic case with negative in middle"),
        ([5, 10, 15], 30, "No negative numbers"),
        ([-5, 1, 2], 0, "Negative at start"),
        ([], 0, "Empty list"),
        ([42], 42, "Single positive number"),
        ([-42], 0, "Single negative number"),
        ([0, 5, 10, -1], 15, "With zeros"),
        ([0, 0, 0], 0, "Only zeros"),
        ([10, 20, -5, 30, 40], 30, "Negative in middle"),
    ]
    
    passed = 0
    failed = 0
    
    for numbers, expected, description in tests:
        print(f"Running test: {description}")
        print(f"  Input: {numbers}")
        result = sum_until_negative(numbers)
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
