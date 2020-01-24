#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    pycolor [color] char -nb
    pycolor [-h | --help]

Options:
    -nb          not bold print
    -h --help    Show this screen and exit.

Note:
    色付き表示
    blue, cyan , green, magenta
    red, white, yellow

    ex)
    cat file | pycolor import
    cat file | pycolor red import | pycolor blue from -nb
"""

def usage():
    print(__doc__)
    exit()

BOLD = True

def main(color, char):
    exec('from fabric.colors import {}'.format(color))
    for row in stdin.readlines():
        print(row.replace(char, eval('{}(char, bold={})'.format(color, True if BOLD else False))), end='')


if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-nb', '--notbold']:
            BOLD = False
            argv.remove(v)

    if len(argv) == 2:
        color, char = 'green', argv[1]
    elif len(argv) == 3:
        color, char = argv[1], argv[2]
    else:
        usage()
    main(color=color, char=char)


