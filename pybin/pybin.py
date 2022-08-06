import argparse
import sys


def main(_str, head, tail):
    for row in sys.stdin.readlines():
        if head and not tail:
            print(_str + row.strip())
        if tail and not head:
            print(row.strip() + _str)
        if head and tail:
            print(_str + row.strip() + _str)


def cli_main():
    parser = argparse.ArgumentParser(description="add str")
    parser.add_argument("str")
    parser.add_argument(
        "-a",
        "--head",
        action="store_true",
        help="Add str in head",
    )
    parser.add_argument(
        "-e",
        "--tail",
        action="store_true",
        help="Add str in tail",
    )
    args = parser.parse_args()
    if args.head or args.tail:
        main(args.str, args.head, args.tail)
    else:
        parser.print_help()
