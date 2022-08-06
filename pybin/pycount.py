import argparse
import sys
import collections


def main():
    data = [row.strip() for row in sys.stdin.readlines()]
    data = collections.Counter(data)
    for key in data:
        print("{}: {}".format(key, data[key]))


def cli_main():
    parser = argparse.ArgumentParser(
        description="count",
    )
    args = parser.parse_args()
    main()
