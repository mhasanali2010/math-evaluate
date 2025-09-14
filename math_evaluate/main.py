import sys
from evaluator import evaluate

def main():
    """Entry point for math-evaluate CLI"""
    import argparse

    parser = argparse.ArgumentParser(
        prog="math",
        description="Evaluate mathematical expressions (with proper BODMAS/PEMDAS)."
    )
    parser.add_argument(
        "expr",
        nargs="?",
        help="Mathematical expression to evaluate"
    )
    parser.add_argument(
        "--eval",
        dest="expression",
        help="Expression passed explicitly (avoids shell quoting issues)"
    )

    args = parser.parse_args()

    # Pick expression from positional arg or --eval
    expr = args.expression or args.expr

    if not expr:
        print("Error: No expression provided.")
        sys.exit(1)

    result = evaluate(expr)
    print(result)
