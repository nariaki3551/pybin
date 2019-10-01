#!/usr/local/bin/python3
from sys import argv, stdin

__doc__ = """
Usage:
	pyremove [-s] str
	pyremove [-h | --help]

Options:
    -s            Strip lines.
    -h --help     Show this screen and exit.

Note:
	入力文字列からstrを取り除く
	ex)
	    ls | pyremove .py
"""

STRIP = False

def usage():
	print(__doc__)
	exit()

def main(_str):
	for row in stdin.readlines():
		if STRIP:
			row = row.stlip()
		else:
			row = row.replace('\n', '')
		print(row.replace(_str, ''))

if __name__ == '__main__':
	for v in argv[1:]:
		if v in ['-h', '--help']:
			usage()
		if v in ['-s']:
			STRIP = True
			argv.remove(v)
	if len(argv) == 2:
		main(_str=argv[1])
	else:
		usage()
