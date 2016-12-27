#!/usr/local/bin/python3
from sys import argv
from DictionaryServices import DCSCopyTextDefinition

__doc__ = """
Usage:
    line [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
    辞書.appで単語を検索
"""

def usage():
    print(__doc__)
    exit()

def main():
    word = argv[1]
    result = DCSCopyTextDefinition(None, word, (0, len(word)))
    try:
        result = result.split('.')
        for row in result:
            print(row)
    except:
        print('その単語は辞書に登録されていません')



if __name__ == '__main__':
    if len(argv) < 2 or argv[1] in ['-h', '--help']:
        usage()
    main()