#!/usr/local/bin/python3
from sys import argv, stdin
import subprocess as sp

__doc__ = """
Usage:
	pywhile COMMAND
	pywhile [-h | --help]

Options:
    -h --help     Show this screen and exit.

Note:
	COMMADN 標準入力を次々と実行
	ex)
	    ls | grep test | pywhile rm
	    ls | grep test | pywhile rm -r
"""

def usage():
	print(__doc__)
	exit()


def main(com):
	for row in stdin.readlines():
		sp.run(com + [row.strip()])


if __name__ == '__main__':
	for v in argv[1:]:
		if v in ['-h', '--help']:
			usage()
	if len(argv) != 1:
		main(com=argv[1:])
	else:
		usage()