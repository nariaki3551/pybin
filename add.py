from sys import argv, stdin

__doc__ = """
Usage:
	add [-a] [-e] str
	add [-h | --help]

Options:
    -a              Add str in head.
    -e              Add str in tail.
    -h --help       Show this screen and exit.

Note:
	入力文字列にstrを追加する
	ex)
	    ls | add \'
"""

HEAD = False
TAIL = False

def usage():
	print(__doc__)
	exit()

def main(_str):
	for row in stdin.readlines():
		if HEAD and not TAIL:
			print(_str+row.strip())
		if TAIL and not HEAD:
			print(row.strip()+_str)
		if HEAD and TAIL:
			print(_str+row.strip()+_str)


if __name__ == '__main__':
	for v in argv[1:]:
		if v in ['-h', '--help']:
			usage()
		if v in ['-a']:
			HEAD = True
			argv.remove('-a')
		if v in ['-e']:
			TAIL = True
			argv.remove('-e')
	if len(argv) == 2 or (HEAD or TAIL):
		main(_str=argv[1])
	else:
		usage()
