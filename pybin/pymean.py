import argparse
import sys

import numpy as np


def main(force, std):
    _sum = 0
    num_data = 0
    if std:
        data = list()
    for row in sys.stdin.readlines():
        row = row.strip()
        try:
            if std:
                data.append(float(row))
            else:
                _sum += float(row)
                num_data += 1
        except:
            if force:
                pass
            else:
                print("error line: {}".format(row))

    if std:
        print(np.mean(data), "\u00B1", np.std(data, ddof=1))
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
    parser.add_argument("--std", action="store_true", help="Convert result to int")
    args = parser.parse_args()

    main(args.force, args.std)
