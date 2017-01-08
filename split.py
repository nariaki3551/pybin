#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    split char
    split [-n] number
    split [-h | --help]

Options:
    -n <number>   numberでstripする。  
    -h --help     Show this screen and exit.

Note:
    標準入力をsplitする。
    ex)
        abc.py | split .     ->  abc py
        abc.py | split -n 2  ->  ab c.py
"""

NUMBER = False

def usage():
    print(__doc__)
    exit()

def main(key):
    for row in stdin.readlines():
        row = row.strip()
        if NUMBER:
            key = int(key)
            try: row = [row[:key], row[key:]]
            except: row = [row]
        else:
            row = row.split(key)
        print(' '.join(row))


if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-n']:
            NUMBER = True
            argv.remove(v)
    if len(argv) == 2:
        main(key=argv[1])
    else:
        usage()