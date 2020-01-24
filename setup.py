import os
import argparse
import subprocess as sp

BIN_DIR = './bin'
scripts = [
    'T',         'pyadd',     'pycolumn',
    'pycorr',    'pyjoin',    'pyline',
    'pymax',     'pymean',    'pymin',
    'pydiv',     'pysort',    'pyremove',
    'pyreplace', 'pyreverse', 'pysplit',
    'pysum',     'pyvar',     'pywhile',
    'pycount',   'pybin',     'pycolor'
]


def main(args):
    rewrite_shebang(args)
    add_permission(args)
    disp_message(args)


def rewrite_shebang(args):
    shebang = '#!'+args.python_path
    print('shebang:', shebang)
    for pyfile in scripts:
        bin_path = BIN_DIR + '/' + pyfile
        sp.getoutput("sed '1d' " + bin_path)
        sp.getoutput("sed -i '{}' {}".format(shebang, bin_path))


def add_permission(args):
    # make symbolic links
    for pyfile in scripts:
        bin_path = BIN_DIR + '/' + pyfile
        print('chmod +x {}'.format(bin_path))
        sp.getoutput('chmod +x {}'.format(bin_path))
    print('\n🍣  ALL COMPLATE')


def disp_message(args):
    message = [
        'make symbolic in ./bin directory,',
        '',
        'please write in your ~/.bash_profile, ~/.bashrc or ~/.zshrc',
        '  or other appropriate file.',
        '',
        '    export PATH={}/bin:${{PATH}}'.format(os.getcwd()),
        ''
    ]
    print('\n'.join(message))


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
