#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    split [-s] str
    split [-h | --help]

Options:
    -s            Strip lines.
    -h --help     Show this screen and exit.

Note:
    標準入力をstrでsplitする
"""

STRIP = False

def usage():
    print(__doc__)
    exit()

def main(_str):
    for row in stdin.readlines():
        if STRIP:
            row = row.strip()
        else:
            row = row.replace('\n', '')
        print(' '.join(row.split(_str)))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-s']:
            STRIP = True
            argv.remove(v)
    if len(argv) == 2:
        main(_str=argv[1])
    else:
        usage()