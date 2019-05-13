#!/usr/local/bin/python3
# ---- memo ---------------------
# [2017-02-10] \|入力を追加
# -------------------------------
from sys import argv, stdin
from collections import defaultdict

__doc__ = """
Usage:
    column [-l] [-a] number or splice
    column [-h | --help]

Options:
    -l              Show column number.
    -a              Arrange.
    -h --help       Show this screen and exit.

Note:
    column [number] でnumber+1列目を表示.
    スライスの入力はpython記法に準ずる.
    ex)
        cat file | column 3
        cat file | column 4:-1
        cat file | column 1\|4\|8: (1, 4行目と8行目以降を表示)
"""

COLUMN = False
ARRANGE = False

def usage():
    print(__doc__)
    exit()


def main(av):
    data = [ row.strip().split() for row in stdin.readlines() ]

    if ARRANGE:
        arr_dict = defaultdict(int)
        for elm in data:
            for col, el in enumerate(elm):
                arr_dict[col] = max(arr_dict[col], len(el))
        data[:] = [ ['{}{}'.format(el, ' '*(arr_dict[col]-len(el))) for col, el in enumerate(elm)] for elm in data]

    if COLUMN:
        data = [ ['[{}] {}'.format(col, el) for col, el in enumerate(elm)] for elm in data]

    if av is None:
        for elm in data:
            print(' '.join(elm))
    else:
        av = av.split('|')
        for elm in data:
            tmp = list()
            for co in av:
                if ':' in co:
                    try:
                        tmp += (eval('elm[{}]'.format(co)))
                    except:
                        tmp.append(' ')
                else:
                    try:
                        tmp.append(eval('elm[{}]'.format(co)))
                    except:
                        tmp.append(' ')
            print(' '.join(tmp))

if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-l']:
            COLUMN = True
            argv.remove('-l')
        if v in ['-a']:
            ARRANGE = True
            argv.remove('-a')
    if len(argv) == 2:
        main(av=argv[1])
    elif COLUMN or ARRANGE:
        main(av=None)
    else:
        usage()