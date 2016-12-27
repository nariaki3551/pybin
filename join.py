#!/usr/local/bin/python3
from sys import stdin, argv

__doc__ = """
Usage:
	join str
    join [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
	標準入力の空白を埋める.
"""

def usage():
	print(__doc__)
	exit()

def main(_str):
	for row in stdin.readlines():
		print(_str.join(row.strip().split()))

if __name__ == '__main__':
	if len(argv) == 2:
		main(_str=argv[1])
	else:
		main(_str='')