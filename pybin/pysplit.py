import argparse
import sys


def main(key):
    for row in sys.stdin.readlines():
        row = row.strip().split(key)
        print(" ".join(row))


def cli_main():
    parser = argparse.ArgumentParser(
        description="split standard input",
    )
    parser.add_argument("str")
    args = parser.parse_args()

    main(args.str)
