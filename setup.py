import os
import argparse
import subprocess as sp

SRC_DIR = './src'
BIN_DIR = './bin'
scripts = [
    'T.py',         'pyadd.py',     'pycolumn.py',
    'pycorr.py',    'pyjoin.py',    'pyline.py',
    'pymax.py',     'pymean.py',    'pymin.py',
    'pydiv.py',     'pysort.py',    'pyremove.py',
    'pyreplace.py', 'pyreverse.py', 'pysplit.py',
    'pysum.py',     'pyvar.py',     'pywhile.py',
    'pycount.py',   'pyif.py',      'pybin.py',
    'pycolor.py'
]


def main(args):
    rewrite_shebang(args)
    make_symbolic(args)


def rewrite_shebang(args):
    shebang = '#!'+args.python_path
    print('shebang:', shebang)
    for pyfile in scripts:
        pyfile_path = SRC_DIR + '/' + pyfile
        sp.getoutput("sed '1d' " + pyfile_path)
        sp.getoutput("sed -i '{}' {}".format(shebang, pyfile_path))


def make_symbolic(args):
    # make symbolic links
    for pyfile in scripts:
        name = pyfile.replace('.py', '')
        pyfile_path = SRC_DIR + '/' + pyfile
        bin_path = BIN_DIR + '/' + name
        print('chmod +x {}'.format(pyfile_path))
        sp.getoutput('chmod +x {}'.format(pyfile_path))
        print('ln -s {} {}'.format(pyfile_path, bin_path))
        sp.getoutput('ln -s {} {}'.format(pyfile_path, bin_path))

    print('\n🍣  ALL COMPLATE')

    description = [
        'make symbolic in ./bin directory,',
        '',
        'please write in your ~/.bash_profile, ~/.bashrc or ~/.zshrc',
        '',
        '    export PATH={}:${{PATH}}'.format(os.getcwd()),
        ''
    ]
    print('\n'.join(description))


def clean():
    for pyfile in scripts:
        name = pyfile.replace('.py', '')
        bin_path = BIN_DIR + '/' + name
        print('unlink {}'.format(bin_path))
        sp.getoutput('unlink {}'.format(bin_path))


def argparser():
    description='make symbolic links for all commands'
    parser = argparse.ArgumentParser(
        prog=__file__,
        description=description
    )
    parser.add_argument(
        '--python_path',
        default=sp.getoutput('which python3'),
        help='python path you use (default: which python3)'
    )
    parser.add_argument(
        '--clean',
        action='store_true',
        help='clear binary files'
    )
    return parser


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()

    if args.clean:
        clean()
    else:
        main(args)
