import argparse
import sys

EXAMPLE = """
ex)
    ls | pyremove .py
"""


def main(_str):
    for row in sys.stdin.readlines():
        row = row.replace("\n", "")
        print(row.replace(_str, ""))


def cli_main():
    parser = argparse.ArgumentParser(
        description="remove a string from standard input",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLE,
    )
    parser.add_argument("str")
    args = parser.parse_args()

    main(args.str)
