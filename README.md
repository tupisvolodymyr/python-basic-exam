# Guideline: How to Implement Solution for Python Tasks

## Prepare the Project

1. **Fork the repository**
   - Go to the repository page on GitHub
   - Click the **Fork** button in the top-right corner

2. **Clone your forked repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-basic-exam.git
   ```
   - Replace `YOUR_USERNAME` with your GitHub username
   - You can get the link by clicking the `Code` button in your repo

3. **Open the project folder in your IDE**
   ```bash
   cd python-basic-exam
   ```

4. **Create a branch for your solution**
   ```bash
   git checkout -b develop
   ```
   - You can use any other name instead of `develop`

5. **Set up virtual environment and install dependencies**
   
   If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
   
   ```bash
   python -m venv venv
   ```
   
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   
   Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Implement the Solution

1. **Implement your solutions** in the `tasks/` folder:
   - `tasks/task1.py` - Sum until negative
   - `tasks/task2.py` - Parse numbers
   - `tasks/task3.py` - Analyze numbers

2. **Test your solution** by running the task file directly:
   ```bash
   python tasks/task1.py
   python tasks/task2.py
   python tasks/task3.py
   ```
   - You'll see which tests pass and which fail
   - Fix your code if any tests fail

3. **Run all tests** with pytest:
   ```bash
   pytest -q
   ```
   - All tests should pass before submitting

4. **Save your solution**
   ```bash
   git add tasks/
   git commit -m "Implement exam solutions"
   ```

5. **Push the solution to your fork**
   ```bash
   git push origin develop
   ```
   - If you created another branch (not `develop`) use its name instead

## Create a Pull Request (PR)

1. **Open your repository on GitHub** and click the **Pull Request** button

2. **Select your branch** (`develop`) in the dropdown

3. **Create the Pull Request**:
   - Base repository: `me1nyk/python-basic-exam`
   - Base branch: `main`
   - Head repository: `YOUR_USERNAME/python-basic-exam`
   - Compare branch: `develop`

4. **Verify the PR details** and confirm

## If Changes Are Requested

1. Make the requested changes in your local files
2. Test again with `pytest -q`
3. Commit and push:
   ```bash
   git add tasks/
   git commit -m "Fix requested changes"
   git push origin develop
   ```
4. The PR will update automatically

## Tips

- Use `print()` statements to debug your code
- Read the function docstrings carefully for requirements
- Test with the examples provided in the docstrings
- Don't modify test files
- Use only basic Python features (no comprehensions, classes, regex)

Good luck! 🚀
