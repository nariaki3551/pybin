#!/usr/local/bin/python3
from sys import argv, stdin
from collections import Counter

__doc__ = """
Usage:
    pycount [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
    標準入力をカウントする
"""

def usage():
    print(__doc__)
    exit()

def main():
    data = [row.strip() for row in stdin.readlines()]
    data = Counter(data)
    for key in data:
        print('{}: {}'.format(key, data[key]))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
    main()
