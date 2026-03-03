# Python Basic Exam

This exam tests your knowledge of basic Python concepts including data types, variables, operators, conditionals, loops, functions, and basic string/list methods.

## Tasks

You need to implement 3 functions in separate files in the `tasks/` folder:

1. **tasks/task1.py** - `sum_until_negative()` - Sum numbers until the first negative number
2. **tasks/task2.py** - `parse_numbers()` - Parse comma-separated numbers from a string
3. **tasks/task3.py** - `analyze_numbers()` - Analyze a list of numbers and return statistics

Each task has its own test file in the `tests/` folder. Run a specific task's tests with `pytest tests/test_task1.py -q` or run all tests with `pytest -q`.

## How to Fork and Submit

### 1. Fork the Repository

1. Go to the repository page on GitHub
2. Click the **Fork** button in the top-right corner
3. This creates a copy of the repository in your GitHub account

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/python-basic-exam.git
cd python-basic-exam
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Implement Your Solutions

Edit the files in the `tasks/` folder (`task1.py`, `task2.py`, `task3.py`) and implement the functions according to their docstrings.

You can work on one task at a time and run it directly to see test results:

```bash
python tasks/task1.py
python tasks/task2.py
python tasks/task3.py
```

Or run all tests at once:

```bash
pytest -q
```

### 5. Test Your Solutions

Run the tests to check if your implementation is correct:

```bash
pytest -q
```

All tests should pass before submitting.

### 6. Commit Your Changes

```bash
git add tasks/
git commit -m "Implement exam solutions"
```

### 7. Push to Your Fork

```bash
git push origin main
```

### 8. Submit

Your solutions are now in your forked repository. Share the link to your fork for evaluation.

## Rules

- Do NOT modify the test files
- Do NOT use list comprehensions, classes, regex, or advanced Python features
- Use only basic Python: loops, conditionals, functions, and basic methods
- All tests must pass

Good luck!
