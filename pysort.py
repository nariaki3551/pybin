#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    pysort [-r | --reverse] [-n]
    pysort [-k | --key] column1 column2 ...
    pysort [-h | --help]

Options:
    -r --reverse    Reverse.
    -k --key        
    -n 
    -i 
    -h --help       Show this screen and exit.

Note:
    標準入力をsortする.
    -k keyを指定できる.
    -n 数字の大小で.
    -i intに変換する.
"""

REVERSE = False
KEY = False
NUMBER = False
INT = False

def usage():
    print(__doc__)
    exit()

def main(key=None):
    data = [ row.strip().split() for row in stdin.readlines() ]
    if key == []:
        if NUMBER:
            data[:] = [ [float(elm) for elm in row] for row in data]
            tmp = sorted(data, reverse=REVERSE)
            if INT:
                tmp[:] = [ [int(elm) for elm in row] for row in tmp ]
            tmp[:] = [ [str(elm) for elm in row] for row in tmp]
        else:
            tmp = sorted(data, reverse=REVERSE)

        for row in tmp:
            print(' '.join(row))


    else:
        if NUMBER:
            tmp = eval('sorted(data, key=lambda x: (float(x[{}])), reverse=REVERSE)'.format(']), float(x['.join(key)))
        else:
            tmp = eval('sorted(data, key=lambda x: (x[{}]), reverse=REVERSE)'.format('], x['.join(key)))

        for row in tmp:
            print(' '.join(row))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-r', '--reverse']:
            REVERSE = True; argv.remove(v)
        if v in ['-k', '--key']:
            KEY = True; argv.remove(v)
        if v in ['-n']:
            NUMBER = True; argv.remove(v)
        if v in ['-i']:
            INT = True; argv.remove(v)
    if KEY and len(argv) < 2:
        usage()
    main(key=argv[1:])