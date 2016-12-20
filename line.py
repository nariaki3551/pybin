from sys import argv, stdin

__doc__ = """
Usage:
	line [-l] number or splice
	line [-h | --help]

Options:
    -l              Show line number.
    -h --help       Show this screen and exit.

Note:
	line [number] でnumber+1行目を表示.
	スライスの入力はpython記法に準ずる.
	ex)
	    cat file | line 3
	    cat file | line 4:-1
"""

LINE = False

def usage():
	print(__doc__)
	exit()


def main(av):
	if LINE:
		data = ['[{}] {}'.format(count, row.strip()) for count, row in enumerate(stdin.readlines())]
	else:
		data = [row.strip() for row in stdin.readlines()]
		

	# 出力
	if av is None:
		for elm in data:
			print(elm)
	else:
		try:
			for elm in eval('data[{}]'.format(av)):
				print(elm)
		except:
			usage()


if __name__ == '__main__':
	if len(argv) < 2:
		usage()

	for v in argv:
		if v in ['-h', '--help']:
			usage()
		if v in ['-l']:
			LINE = True
			argv.remove('-l')
	if len(argv) == 2:
		main(av=argv[1])
	elif LINE:
		main(av=None)
	else:
		usage()