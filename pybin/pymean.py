import argparse
import sys


def main(force, float2int):
    _sum = 0
    num_data = 0
    for row in sys.stdin.readlines():
        row = row.strip()
        try:
            _sum += float(row)
            num_data += 1
        except:
            if force:
                pass
            else:
                print("error line: {}".format(row))

    if float2int:
        print(_sum // num_data)
    else:
        print(_sum / num_data)


def cli_main():
    description = """
        output mean value.
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
