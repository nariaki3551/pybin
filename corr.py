#!/usr/local/bin/python3
from sys import argv, stdin
import numpy as np
from itertools import combinations

__doc__ = """
Usage:
	corr [-p | --parametor] [-a | --all] int int (int is line number)
	corr [-h | --help]

Options:
    -p              Show parametor.
    -a --all        Calculate corr all parametors pairs.
    -h --help       Show this screen and exit.

Note:
	int 行目と int行目の相関係数を出力する.
	標準入力はcsvファイルを想定.
	オプション-pを使用する時は、入力ファイルの1列目はパラメータ名.
"""

ALL = False
PARAMETOR = False

def usage():
	print(__doc__)
	exit()

def main(colA, colB):
	# データ入力
	is_first = True
	for row in stdin.readlines():
		if is_first:
			num_column = len(row.strip().split())
			data = [ list() for _ in range(num_column) ]
			is_first = False
			if PARAMETOR:
				para_list = row.strip().split()
				continue
		for i, elm in enumerate(row.strip().split()):
			try:
				data[i].append(float(elm))
			except:
				pass

	if ALL:
		for colA, colB in combinations(range(num_column), 2):
			corr = np.corrcoef(data[colA], data[colB])[0, 1]
			if PARAMETOR:
				print('{} {}: {}'.format(para_list[colA], para_list[colB], corr))
			else:
				print(corr)
	else:
		corr = np.corrcoef(data[colA], data[colB])[0, 1]
		if PARAMETOR:
			print('{} {}: {}'.format(para_list[colA], para_list[colB], corr))
		else:
			print(corr)

if __name__ == '__main__':
	for v in argv[1:]:
		if v in ['-h', '--help']:
			usage()
		if v in ['-a', '--all']:
			ALL = True
			argv.remove(v)
		if v in ['-p', '--parametor']:
			PARAMETOR = True
			argv.remove(v)
	if not ALL and len(argv) == 3:
		main(int(argv[1]), int(argv[2]))
	elif ALL:
		main(0, 0)
	else:
		usage()


