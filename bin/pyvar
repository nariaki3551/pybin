#!/usr/local/bin/python3
from sys import argv, stdin
from numpy import var

__doc__ = """
Usage:
    pyvar [-f]
    pyvar [-d | --ddof] 0 or 1
    pyvar [-h | --help]

Options:
    -f              Don't show error message.
    -d --ddof       Select Specimen(0) or Unbiased(1). Default is Specimen.
    -h --help       Show this screen and exit.

Note:
    標準入力の数字の分散を出力する.
    標準入力が数字以外の場合、その行を飛ばす.
    -d 0 で標本分散, -d 1で不偏分散を計算.
"""

FORCE = False
DDOF = False

def usage():
    print(__doc__)
    exit()

def main(ddof):
    data = list()
    for row in stdin.readlines():
        row = row.strip()
        try:
            data.append(float(row))
        except:
            if FORCE:
                pass
            else:
                print('error line: {}'.format(row))

    print(var(data, ddof=ddof))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-f']:
            FORCE = True
            argv.remove(v)
        if v in ['-d', '--ddof']:
            DDOF = True
            argv.remove(v)
    if DDOF and len(argv) == 2:
        main(ddof=int(argv[1]))
    elif not DDOF:
        main(ddof=0)
    else:
        usage()


