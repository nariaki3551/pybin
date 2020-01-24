#!/usr/local/bin/python3
# ---- memo ---------------------
# [2017-02-10] \|入力を追加
# -------------------------------
from sys import argv, stdin
from collections import defaultdict

__doc__ = """
Usage:
    pycolumn [-l] [-a] [-at] number or splice
    pycolumn [-h | --help]

Options:
    -l              Show column number.
    -a              Arrange (head).
    -at             Arrange (tail).
    -h --help       Show this screen and exit.

Note:
    pycolumn [number] でnumber+1列目を表示.
    スライスの入力はpython記法に準ずる.
    ex)
        cat file | pycolumn 3
        cat file | pycolumn 4:-1
        cat file | pycolumn 1\|4\|8: (1, 4行目と8行目以降を表示)
"""

COLUMN = False
ARRANGE = False
ARRANGE_TAIL = False

def usage():
    print(__doc__)
    exit()


def main(av):
    data = [ row.strip().split() for row in stdin.readlines() ]

    if ARRANGE or ARRANGE_TAIL:
        arr_dict = defaultdict(int)
        for elm in data:
            for col, el in enumerate(elm):
                arr_dict[col] = max(arr_dict[col], len(el))
        if ARRANGE:
            data[:] = [ ['{}{}'.format(el, ' '*(arr_dict[col]-len(el))) for col, el in enumerate(elm)] for elm in data]
        else:
            data[:] = [ ['{}{}'.format(' '*(arr_dict[col]-len(el)), el) for col, el in enumerate(elm)] for elm in data]

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
        if v in ['-at']:
            ARRANGE_TAIL = True
            argv.remove('-at')
    if len(argv) == 2:
        main(av=argv[1])
    elif COLUMN or ARRANGE or ARRANGE_TAIL:
        main(av=None)
    else:
        usage()
