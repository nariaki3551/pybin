import argparse
import sys


def main(force, float2int):
    data = list()
    _max = -float("inf")
    for row in sys.stdin.readlines():
        row = row.strip()
        try:
            _max = max(_max, float(row))
        except:
            if force:
                pass
            else:
                print("error line: {}".format(row))

    if float2int:
        print(int(_max))
    else:
        print(_max)


def cli_main():
    description = """
        output max value.
        if input line is not number, the line is ignore"""

    parser = argparse.ArgumentParser(
        description=description,
    )
    parser.add_argument(
        "-f", "--force", action="store_true", help="Do not show error message"
    )
    parser.add_argument(
        "-i", "--int", action="store_true", help="Convert result to int"
    )
    args = parser.parse_args()

    main(args.force, args.int)
