import argparse

from math_evaluate.evaluator import evaluate

def init_argument_parser() -> argparse.Namespace:
    """Function to initialize the Argument Parser"""
    parser = argparse.ArgumentParser(description='evaluates mathematical expressions while following BODMAS/PEMDAS')
    parser.add_argument("--eval", type=str, required=True, help="Evaluate given expression")
    args = parser.parse_args()

    return args


def main() -> None:
    try:
        args = init_argument_parser()
        expr = args.eval
        result = evaluate(expr)
        print(f'RESULT: {result}')
    except SystemExit:
        print('Error: failed to parse arguments')


if __name__ == '__main__':
    main()