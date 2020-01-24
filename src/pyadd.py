#!/usr/local/bin/python3
# ---- memo ---------------------
# [2017-01-20] オプション -n を追加
# -------------------------------
from sys import argv, stdin

__doc__ = """
Usage:
    pyadd [-a] [-e] str
    pyadd [-n] start_number
    pyadd [-h | --help]

Options:
    -a              Add str in head.
    -e              Add str in tail.
    -n              Add number.
    -h --help       Show this screen and exit.

Note:
    入力文字列にstrを追加する
    ex)
        ls | pyadd -a \'
        ls | pyadd -e -n 0
"""

HEAD = False
TAIL = False
NUM = False

def usage():
    print(__doc__)
    exit()

def main(_str):
    for row in stdin.readlines():
        if HEAD and not TAIL:
            print(_str+row.strip())
        if TAIL and not HEAD:
            print(row.strip()+_str)
        if HEAD and TAIL:
            print(_str+row.strip()+_str)

def main2(start_num):
    count = start_num
    for row in stdin.readlines():
        if HEAD and not TAIL:
            print(str(count)+row.strip())
        if TAIL and not HEAD:
            print(row.strip()+str(count))
        if HEAD and TAIL:
            print(str(count)+row.strip()+str(count))
        count += 1


if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-a']:
            HEAD = True
            argv.remove('-a')
        if v in ['-e']:
            TAIL = True
            argv.remove('-e')
        if v in ['-n']:
            NUM = True
            argv.remove('-n')
    if NUM:
        main2(start_num=int(argv[1]))
        exit()
    if len(argv) == 2 or (HEAD or TAIL):
        main(_str=argv[1])
    else:
        usage()
