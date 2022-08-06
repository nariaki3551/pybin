import argparse
import sys


def main(force, float2int):
    _sum = 0
    for row in sys.stdin.readlines():
        row = row.strip()
        try:
            _sum += float(row)
        except:
            if force:
                pass
            else:
                print("error line: {}".format(row))

    if float2int:
        print(int(_sum))
    else:
        print(_sum)


def cli_main():
    description = """
        output sum value.
        if input line is not number, the line is ignore."""

    parser = argparse.ArgumentParser(
        description=description,
    )
    parser.add_argument("-f", "--force", action="store_true", help="エラーメッセージを表示しない")
    parser.add_argument("-i", "--int", action="store_true", help="intに変換する")
    args = parser.parse_args()

    main(args.force, args.int)
