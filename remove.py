from sys import argv, stdin

__doc__ = """
Usage:
	remove str
	remove [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
	入力文字列からstrを取り除く
	ex)
	    ls | remove .py
"""


def usage():
	print(__doc__)

def main(_str):
	for row in stdin.readlines():
		print(row.strip().replace(_str, ''))

if __name__ == '__main__':
	if len(argv) < 2 or argv[1] in ['-h', '--help']:
		usage()
	else:
		main(_str=argv[1])