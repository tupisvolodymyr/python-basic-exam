def build_passed_students_map(records: list[dict]) -> dict[str, int]:
    return {
        student["name"].strip() : student["score"]
        for student in records
        if student["score"] >= 60
    }
    '''
    Build a dictionary of passing students using dict comprehension.
    
    Rules:
    - Include only students with score >= 60
    - Use the stripped student name as the key
    - Use the score as the value
    
    Args:
        records: A list of dictionaries, each containing "name" and "score"
        
    Returns:
        A dictionary mapping student names to their scores (only passing students)
        
    Example:
        """">>> records = [
        ...     {"name": " Alice ", "score": 75},
        ...     {"name": "Bob", "score": 50},
        ...     {"name": " Clara ", "score": 90}
        ... ]
         """">>> build_passed_students_map(records)
        {"Alice": 75, "Clara": 90} '''
