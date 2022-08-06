import argparse
import statistics
import sys


def main(force):
    data = list()
    for row in sys.stdin.readlines():
        row = row.strip()
        try:
            data.append(float(row))
        except:
            if force:
                pass
            else:
                print("error line: {}".format(row))

    print("num_data     {}".format(len(data)))
    print("min          {}".format(min(data)))
    print("max          {}".format(max(data)))
    print("mean         {}".format(statistics.mean(data)))
    print("median       {}".format(statistics.median(data)))
    print("variance     {}".format(statistics.variance(data)))
    print("stdev        {}".format(statistics.stdev(data)))


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
    args = parser.parse_args()

    main(args.force)
