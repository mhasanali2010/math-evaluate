import argparse

from evaluator import evaluate

def init_argument_parser() -> argparse.Namespace:
    """Function to initialize the Argument Parser"""
    parser = argparse.ArgumentParser(description='evaluates mathematical expressions while following BODMAS/PEMDAS')
    parser.add_argument("--eval", type=str, required=True, help="Evaluate given expression")
    args = parser.parse_args()

    return args


def main() -> None:
    args = init_argument_parser()
    expr = args.eval
    result = evaluate(expr)
    print("Note:")
    print(" - This evaluator follows BODMAS/PEMDAS.")
    print(" - Division and multiplication are evaluated left to right, same for addition and subtraction.")
    print(" - Exponent associativity is not supported.")
    print(" - Use brackets () if you want to force evaluation order.")
    print(f'RESULT: {result}')


if __name__ == '__main__':
    main()