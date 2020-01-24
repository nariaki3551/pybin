#!/usr/bin/env python3
import subprocess as sp
from sys import argv

__doc__='''
Usage:
        python3 setup.py [--reset]

Note:
        install python packaage and
        make symbolic links for all commands.
'''

scripts \
    = ['T.py',
       'pyadd.py',
       'pycolumn.py',
       'pycorr.py',
       'pyjoin.py',
       'pyline.py',
       'pymax.py',
       'pymean.py',
       'pymin.py',
       'pydiv.py',
       'pysort.py',
       'pyremove.py',
       'pyreplace.py',
       'pyreverse.py',
       'pysplit.py',
       'pysum.py',
       'pyvar.py',
       'pywhile.py',
       'pycount.py',
       'pyif.py',
       'pybin.py',
       'pycolor.py'
      ]

def main():
    try:
      # install python package
      sp.run(['pip3', 'install', 'numpy'])
      sp.run(['pip3', 'install', 'fabric3'])


      # make symbolic links
      for file in scripts:
          print('chmod +x {}'.format(file))
          sp.getoutput('chmod +x {}'.format(file))
          print('ln -s {} {}'.format(file, file.replace('.py', '')))
          sp.getoutput('ln -s {} {}'.format(file, file.replace('.py', '')))
    except:
      print('\n ERROR'); exit()

    print('\n🍣  ALL COMPLATE')

def reset():
    for file in scripts:
        print('unlink {}'.format(file.replace('.py', '')))
        sp.getoutput('unlink {}'.format(file.replace('.py', '')))    

if __name__ == '__main__':
    if '--reset' in argv:
      reset()
    else:
      main()
