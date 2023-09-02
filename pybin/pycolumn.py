import argparse
import sys
import collections

EXAMPLE = """
ex)
    cat file | pycolumn -s 3
    cat file | pycolumn -s 4:-1
    cat file | pycolumn -s 1\|4\|8: (print 1 line and 4--8 lines)
"""


def main(av, column, arrange, arrange_tail):
    data = [row.strip().split() for row in sys.stdin.readlines()]

    if arrange or arrange_tail:
        arr_dict = collections.defaultdict(int)
        for elm in data:
            for col, el in enumerate(elm):
                arr_dict[col] = max(arr_dict[col], len(el))
        if arrange:
            data[:] = [
                [
                    "{}{}".format(el, " " * (arr_dict[col] - len(el)))
                    for col, el in enumerate(elm)
                ]
                for elm in data
            ]
        else:
            data[:] = [
                [
                    "{}{}".format(" " * (arr_dict[col] - len(el)), el)
                    for col, el in enumerate(elm)
                ]
                for elm in data
            ]

    if column:
        data = [
            ["[{}] {}".format(col, el) for col, el in enumerate(elm)] for elm in data
        ]

    if av is None:
        for elm in data:
            print(" ".join(elm))
    else:
        av = av.split("|")
        for elm in data:
            tmp = list()
            for co in av:
                if ":" in co:
                    try:
                        tmp += eval("elm[{}]".format(co))
                    except:
                        tmp.append(" ")
                else:
                    try:
                        tmp.append(eval("elm[{}]".format(co)))
                    except:
                        tmp.append(" ")
            print(" ".join(tmp))


def cli_main():
    parser = argparse.ArgumentParser(
        description="pycolumn [number or slice]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLE,
    )
    parser.add_argument(
        "-s", "--slice", default=None, help="number or splice (default None)"
    )
    parser.add_argument("-l", action="store_true", help="Show column number")
    parser.add_argument("-a", action="store_true", help="Arrange (head)")
    parser.add_argument("-at", action="store_true", help="Arrange (tail)")
    args = parser.parse_args()

    main(args.slice, args.l, args.a, args.at)
