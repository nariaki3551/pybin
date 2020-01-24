#!/usr/local/bin/python3

from sys import argv, stdin

__doc__ = """
Usage:
    pyif [条件式]

Options:
    -h --help       Show this screen and exit.

Note:
    [条件式]を満たす行を出力する
    $ cat test.txt
    a 1
    b 1
    c 1
    d 2
    e 3
    f 2

    $ cat test.txt | pyif 'float(row[1])>=2' 　等...
"""


def usage():
    print(__doc__)
    exit()

def main(condi):
    for row in stdin.readlines():
        row = row.split()
        if eval(condi):
            print(' '.join(row))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()

    if len(argv) == 2:
        main(condi=argv[1])
    else:
        usage()
