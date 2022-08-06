import argparse
import sys


def main():
    data = [row.strip().split() for row in sys.stdin.readlines()]
    column_max = max([len(row) for row in data])
    for _ in range(column_max):
        for elm in data:
            try:
                print(elm[_], end=" ")
            except:
                print("-", end=" ")
        print()


def cli_main():
    parser = argparse.ArgumentParser(description="transpose between row and column")
    args = parser.parse_args()
    main()
