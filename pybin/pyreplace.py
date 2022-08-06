import argparse
import sys
import subprocess

EXAMPLE = """
ex)
    ls | pyreplace .py .java
    ls | pyreplace .py .java --mv
"""


def main(strA, strB, mv):
    for row in sys.stdin.readlines():
        row = row.replace("\n", "")
        print(row.replace(strA, strB))
        if mv:
            subprocess.run(["mv", row, row.replace(strA, strB)])


def cli_main():
    parser = argparse.ArgumentParser(
        description="入力文字列のstrAをstrBに置き換える",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLE,
    )
    parser.add_argument("strA")
    parser.add_argument("strB")
    parser.add_argument(
        "--mv", action="store_true", help="run command `mv original replaced`"
    )
    args = parser.parse_args()

    main(args.strA, args.strB, args.mv)
