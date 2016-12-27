#!/usr/bin/env python3

import subprocess as sp
import os.path

__doc__='''
Usage:
    python3 setup.py
    
Note:
    make symbolic links for all commands.
'''

scripts = ['T.py',
           'add.py',
           'column.py',
           'corr.py',
           'dict.py',
           'join.py',
           'line.py',
           'max.py',
           'mean.py',
           'min.py',
           'pysort.py',
           'remove.py',
           'replace.py',
           'reverse.py',
           'split.py',
           'sum.py',
           'var.py'
          ]



def main():
	for file in scripts:
		sp.run(['ln', '-s', file, file.replace('.py', '')])
	print('OK')


if __name__ == '__main__':
	main()