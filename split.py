#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
	split str
    split [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
	標準入力をstrでsplitする
"""

def usage():
	print(__doc__)
	exit()

def main(_str):
	for row in stdin.readlines():
		print(' '.join(row.strip().split(_str)))

if __name__ == '__main__':
	for v in argv[1:]:
		if v in ['-h', '--help']:
			usage()
	if len(argv) == 2:
		main(_str=argv[1])
	else:
		usage()