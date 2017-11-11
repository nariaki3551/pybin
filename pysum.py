#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    sum [-f] [-i]
    sum [-h | --help]

Options:
    -f              Don't show error message.
    -i              Convert result to int.
    -h --help       Show this screen and exit.

Note:
    標準入力の数字の和を出力する.
    標準入力が数字以外の場合、その行を飛ばす.
"""

FORCE = False
FLOAT2INT = False

def usage():
    print(__doc__)
    exit()

def main():
    _sum = 0
    for row in stdin.readlines():
        row = row.strip()
        try:
            _sum += float(row)
        except:
            if FORCE:
                pass
            else:
                print('error line: {}'.format(row))
                
    if FLOAT2INT:
        print(int(_sum))
    else:
        print(_sum)

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-f']:
            FORCE = True
        if v in ['-i']:
            FLOAT2INT = True
    main()