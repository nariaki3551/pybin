#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    reverse [-s]
    reverse [-h | --help]

Options:
    -s              Strip lines.
    -h --help       Show this screen and exit.

Note:
    逆順表示
    ex)
        cat file | reverse
"""

STRIP = False

def usage():
    print(__doc__)
    exit()

def main():
    if STRIP:
        data = [ row.strip() for row in stdin.readlines() ]
    else:
        data = [ row.replace('\n', '') for row in stdin.readlines() ]

    for row in data[::-1]:
        print(row)


if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-s']:
            STRIP = True
            argv.remove(v)
    main()