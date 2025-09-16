# Mathematical Expression Evaluator (math-evaluate)
## By mhasanali2010

## PyPI project link
https://pypi.org/project/math-evaluate

## About the project
A simple command-line calculator for quick math without leaving the terminal.
## Installation
Install using:
```bash
pip install math-evaluate
```

## Usage
Example usage:
```bash
math "10*(5-2)^2 / 3"
```
Output: `30`
### Using the Evaluator for your own Projects
In order to use the mathematical expression evaluator in your own projects, follow these steps:
- Set up a virtual environment in your project folder (Optional):
    ```bash
    python -m venv venv
    source venv/bin/activate # for macOS/Linux
    venv\Scripts\activate.bat # for windows CMD
    .\venv\Scripts\activate.bat # for windows Powershell
    ```
- Install math-evaluate using pip:
    ```bash
    pip install math-evaluate
    ```
- Now, in your code add this line:
    ```python
    from math_evaluate.evaluator import evaluate
    ```
- Now, you can call the evaluator function to return a string which can be an error message or result while giving it the mathematical expression as argument:
    ```python
    result = evaluate("5+5")
    print(result, type(result)
    ```
    Output: `10 <class 'str'>`
## Testing
- Unittests have been included in `./tests.py`
- Running tests:
    1. Clone the repository:
        ```bash
        git clone https://github.com/mhasanali2010/math-evaluate
        ```
    2. Navigate to the repository:
        ```bash
        cd math-evaluate
        ```
    3. Run the tests:
        ```bash
        python tests.py
        ```

## Notes
- Supported operators: +, -, *, /, (, ), ^
- This evaluator follows BODMAS/PEMDAS.
- Division and multiplication are evaluated left to right, same for addition and subtraction.
- Exponent associativity is supported.
- Use brackets () if you want to force evaluation order.
- Requires `Python 3.10` or later.
- Argument Parsing might glitch when using `zsh` if you try to evaluate an expression which contains `-(`.
    - If this happens then run the script using:
        ```bash
        math --eval="<expression>"
        ```
- The CLI command is installed as `math`.
