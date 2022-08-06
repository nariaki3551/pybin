import argparse
import sys


def main(_str):
    for row in sys.stdin.readlines():
        print(_str.join(row.split()))


def cli_main():
    parser = argparse.ArgumentParser(
        description="join",
    )
    parser.add_argument("str")
    args = parser.parse_args()

    main(_str=args.str)
