#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    pyreplace [-s] strA strB
    pyreplace [-h | --help]

Options:
    -s            Strip lines.
    -h --help     Show this screen and exit.

Note:
    入力文字列のstrAをstrBに置き換える
    ex)
        pyreplace .py .java
"""

STRIP = False

def usage():
    print(__doc__)
    exit()

def main(strA, strB):
    for row in stdin.readlines():
        if STRIP:
            row = row.strip()
        else:
            row = row.replace('\n', '')
        print(row.replace(strA, strB))

if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-s']:
            STRIP = True
            argv.remove(v)
    if len(argv) == 3:
        main(strA=argv[1], strB=argv[2])
    else:
        usage()
