#!/usr/local/bin/python3
from sys import argv

def usage():
    pass

LIST = False

def main():
    if LIST:
        LIST_print()


def LIST_print():
    scripts = ['T.py',
               'add.py',
               'column.py',
               'corr.py',
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
               'var.py',
               'pywhile.py',
               'count.py',
               'pyif.py'
               ]
    for script in scripts:
        print(script.replace('.py', ''))




if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['list']:
            LIST = True
            argv.remove(v)
            main()
