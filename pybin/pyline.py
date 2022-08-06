import argparse
import sys

EXAMPLE = """
ex)
    cat file | pyline -s 3
    cat file | pyline -s 4:-1
    cat file | pyline -s 4:-1\|2\|0
"""


def main(av, line):
    data = [row.replace("\n", "") for row in sys.stdin.readlines()]
    if line:
        data[:] = ["[{}] {}".format(count, row) for count, row in enumerate(data)]

    # 出力
    if av is None:
        for elm in data:
            print(elm)
        exit()

    # if av not in None
    if av.replace("-", "").isdigit():
        print(data[int(av)])
    else:
        av = av.split("|")
        output_data = list()
        for li in av:
            tmp_data = eval("data[{}]".format(li))
            if isinstance(tmp_data, list):
                output_data += tmp_data
            else:
                output_data += [tmp_data]

        for elm in output_data:
            print(elm)


def cli_main():
    parser = argparse.ArgumentParser(
        description="line [number or slice]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLE,
    )
    parser.add_argument(
        "-s", "--slice", default=None, help="number or splice (default None)"
    )
    parser.add_argument("-l", action="store_true", help="Show line number")
    args = parser.parse_args()
    main(args.slice, args.l)
