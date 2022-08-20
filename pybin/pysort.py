import argparse
import sys


def main(key, number, to_int, reverse):
    data = [row.strip().split() for row in sys.stdin.readlines()]
    if key == -100:
        if number:
            data[:] = [[float(elm) for elm in row] for row in data]
            tmp = sorted(data, reverse=reverse)
            if to_int:
                tmp[:] = [[int(elm) for elm in row] for row in tmp]
            tmp[:] = [[str(elm) for elm in row] for row in tmp]
        else:
            tmp = sorted(data, reverse=reverse)

        for row in tmp:
            print(" ".join(row))

    else:
        if number:
            tmp = eval(
                "sorted(data, key=lambda x: (float(x[{}])), reverse=reverse)".format(
                    key
                )
            )
        else:
            tmp = eval(
                "sorted(data, key=lambda x: (x[{}]), reverse=reverse)".format(key)
            )

        for row in tmp:
            print(" ".join(row))


def cli_main():
    parser = argparse.ArgumentParser(
        description="sort standard input",
    )
    parser.add_argument(
        "-k", "--key", type=int, default=-100, help="int 列目をkeyにしてsortする"
    )
    parser.add_argument("-n", "--number", action="store_true", help="数字によりsortする")
    parser.add_argument("-i", "--int", action="store_true", help="intに変換する")
    parser.add_argument("-r", "--reverse", action="store_true", help="降順にsortする")
    args = parser.parse_args()

    main(args.key, args.number, args.int, args.reverse)
