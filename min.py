from sys import argv, stdin

__doc__ = """
Usage:
	min [-f]
	min [-h | --help]

Options:
	-f              Don't show error message.
    -h --help       Show this screen and exit.

Note:
	標準入力の数字の最小値を出力する.
	標準入力が数字以外の場合、その行を飛ばす.
"""

FORCE = False

def usage():
	print(__doc__)
	exit()

def main():
	data = list()
	_min = float('inf')
	for row in stdin.readlines():
		row = row.strip()
		try:
			_min = min(_min, float(row))
		except:
			if FORCE:
				pass
			else:
				print('error line: {}'.format(row))
	print(_min)

if __name__ == '__main__':
	for v in argv[:]:
		if v in ['-h', '--help']:
			usage()
		if v in ['-f']:
			FORCE = True
	main()