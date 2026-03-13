def clean_words(words: list[str]) -> list[str]:
    return [
        word.strip().lower()
        for word in words
        if word.strip()
    ]



'''
   Clean and filter a list of words using list comprehension.
pytest test_task_01_clean_words.py
    Rules:
    - Strip whitespace from each word
    - Convert each word to lowercase
    - Keep only words that are not empty after stripping

    Args:
        words: A list of strings that may contain leading/trailing spaces

    Returns:
        A new list with cleaned, lowercase, non-empty words

    Example:
        >>> clean_words([" Hello ", "WORLD", "   ", " Python "])
        ["hello", "world", "python"] '''


