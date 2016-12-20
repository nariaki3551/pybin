from sys import argv, stdin

__doc__ = """
Usage:
	replace strA strB 
	replace [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
	入力文字列のstrAをstrBに置き換える
	ex)
	    replace .py .java
"""


def usage():
	print(__doc__)
	exit()

def main(strA, strB):
	for row in stdin.readlines():
		row = row.strip()
		print(row.replace(strA, strB))

if __name__ == '__main__':
	for v in argv[:]:
		if v in ['-h', '--help']:
			usage()
	if len(argv) == 3:
		main(strA=argv[1], strB=argv[2])
	else:
		usage()