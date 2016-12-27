#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
    row [-l] [-v] [-s] number or splice
    row [-h | --help]

Options:
    -s            Strip lines.  
    -l            Show line number.
    -h --help     Show this screen and exit.

Note:
    line [number] でnumber+1行目を表示.
    スライスの入力はpython記法に準ずる.
    ex)
        cat file | line 3
        cat file | line 4:-1
"""

LINE = False
STRIP = False

def usage():
    print(__doc__)
    exit()


def main(av):
    data = [row.replace('\n', '') for row in stdin.readlines()]
    if STRIP:
        data[:] = [row.strip() for row in data]
    if LINE:
        data[:] = ['[{}] {}'.format(count, row) for count, row in enumerate(data)]

    # 出力
    if av is None:
        for elm in data:
            print(elm)
    else:
        if av.replace('-', '').isdigit():
            print(data[int(av)])
        else:
            try:
                for elm in eval('data[{}]'.format(av)):
                    print(elm)
            except:
                usage()


if __name__ == '__main__':
    if len(argv) < 2:
        usage()

    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-l']:
            LINE = True
            argv.remove(v)
        if v in ['-s']:
            STRIP = True
            argv.remove(v)
    if len(argv) == 2:
        main(av=argv[1])
    elif LINE:
        main(av=None)
    else:
        usage()