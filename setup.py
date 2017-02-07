#!/usr/bin/env python3
import subprocess as sp

__doc__='''
Usage:
        python3 setup.py
        
Note:
        install python packaage
        make symbolic links for all commands.
'''

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



def main():
    try:
      # install python package
      print(sp.getoutput('pip3 install numpy'))

      # make symbolic links
      for file in scripts:
          sp.getoutput('chmod +x {}'.format(file))
          print('chmod +x {}'.format(file))
          sp.getoutput('ln -s {} {}'.format(file, file.replace('.py', '')))
          print('ln -s {} {}'.format(file, file.replace('.py', '')))
    except:
      print('\n ERROR'); exit()

    print('\n🍣  ALL COMPLATE')


if __name__ == '__main__':
    main()