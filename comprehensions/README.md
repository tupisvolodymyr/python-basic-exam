# Python Comprehensions Homework

A beginner-to-intermediate Python homework assignment focusing on list and dict comprehensions.

## Tasks

You will implement three functions:

1. **task_01_clean_words.py** - Clean and filter a list of words using list comprehension
2. **task_02_passed_students.py** - Build a dictionary of passing students using dict comprehension
3. **task_03_flatten_even_numbers.py** - Flatten a matrix and filter even numbers using nested list comprehension

Each task file contains a function stub with a detailed docstring. Read the docstring carefully and implement the function using comprehensions.

## Setup

### 1. Fork this repository

Click the "Fork" button at the top right of this repository page.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/python-comprehensions-homework.git
cd python-comprehensions-homework
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Working on the homework

1. Open the files in `src/` directory
2. Read the docstrings carefully
3. Replace `raise NotImplementedError` with your solution
4. Use comprehensions (list or dict) as specified in each task
5. Run tests to verify your solution

## Running tests

Run all tests:

```bash
pytest
```

Run tests for a specific task:

```bash
pytest tests/test_task_01_clean_words.py
pytest tests/test_task_02_passed_students.py
pytest tests/test_task_03_flatten_even_numbers.py
```

Run tests with `-s` flag to see print statements:
```bash
pytest -s
pytest tests/test_task_01_clean_words.py -s
```

## Submitting your work

### 1. Create a new branch

```bash
git checkout -b solution
```

### 2. Commit your changes

```bash
git add src/
git commit -m "Implement comprehension tasks"
```

### 3. Push to your fork

```bash
git push origin solution
```

### 4. Create a Pull Request

1. Go to your fork on GitHub
2. Click "Pull requests" → "New pull request"
3. Select `base repository: original-repo` and `compare: solution`
4. Click "Create pull request"
5. Add a title and description
6. Submit the pull request

## Requirements

- Python 3.11+
- All solutions must use comprehensions (no loops)
- All tests must pass

Good luck!
