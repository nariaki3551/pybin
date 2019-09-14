#!/usr/bin/env python3
import subprocess as sp

__doc__='''
Usage:
        python3 setup.py

Note:
        install python packaage and
        make symbolic links for all commands.
'''

scripts \
    = ['T.py',
       'add.py',
       'pycolumn.py',
       'corr.py',
       'pyjoin.py',
       'pyline.py',
       'max.py',
       'mean.py',
       'min.py',
       'pysort.py',
       'remove.py',
       'replace.py',
       'reverse.py',
       'split.py',
       'pysum.py',
       'var.py',
       'pywhile.py',
       'count.py',
       'pyif.py',
       'pybin.py',
       'color.py'
      ]



def main():
    try:
      # install python package
      sp.run(['pip3', 'install', 'numpy'])
      sp.run(['pip3', 'install', 'fabric'])


      # make symbolic links
      for file in scripts:
          print('chmod +x {}'.format(file))
          sp.getoutput('chmod +x {}'.format(file))
          print('ln -s {} {}'.format(file, file.replace('.py', '')))
          sp.getoutput('ln -s {} {}'.format(file, file.replace('.py', '')))
    except:
      print('\n ERROR'); exit()

    print('\n🍣  ALL COMPLATE')


if __name__ == '__main__':
    main()
