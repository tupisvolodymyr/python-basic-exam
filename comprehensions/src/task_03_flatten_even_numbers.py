def flatten_even_numbers(matrix: list[list[int]]) -> list[int]:
    return [
        num
        for row in matrix
        for num in row
        if num % 2 == 0
    ]
    """
    Flatten a matrix and filter even numbers using nested list comprehension.
    
    Rules:
    - Go through all rows
    - Take all numbers from all rows
    - Keep only even numbers
    - Preserve the original order
    
    Args:
        matrix: A list of lists containing integers
        
    Returns:
        A flat list containing only the even numbers from the matrix
        
    Example:
        >>> flatten_even_numbers([[1, 2, 3], [4, 5], [6]])
        [2, 4, 6]
    """
