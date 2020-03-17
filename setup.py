import os
import argparse
import subprocess as sp

BIN_DIR = './bin'
scripts = [
    'T',         'pyadd',     'pycolumn',
    'pycorr',    'pyjoin',    'pyline',
    'pymax',     'pymean',    'pymin',
    'pysort',    'pyremove',  'pyreplace',
    'pyreverse', 'pysplit',   'pysum',
    'pyvar',     'pywhile',   'pycount',
    'pycolor',
    'hist'
]


def main(args):
    rewrite_shebang(args)
    add_permission(args)
    disp_message(args)


def rewrite_shebang(args):
    shebang = '#!'+args.python_path+'\n'
    print('\nshebang:', shebang)
    for pyfile in scripts:
        bin_path = BIN_DIR + '/' + pyfile
        lines = list(open(bin_path, 'r'))
        lines[0] = shebang
        sp.getoutput('rm ' + bin_path)
        with open(bin_path, 'w') as f:
            for line in lines:
                f.write(line)


def add_permission(args):
    for pyfile in scripts:
        bin_path = BIN_DIR + '/' + pyfile
        sp.getoutput('chmod +x {}'.format(bin_path))


def disp_message(args):
    message = [
        '',
        'Please write following in your ~/.bash_profile, ~/.bashrc, ~/.zshrc',
        '  or other appropriate file.',
        '',
        '    export PATH={}/bin:${{PATH}}'.format(os.getcwd()),
        ''
    ]
    print('\n'.join(message))


def argparser():
    description='make symbolic links for all commands'
    parser = argparse.ArgumentParser(
        prog=__file__,
        description=description,
        add_help=True
    )
    parser.add_argument(
        '--python_path',
        default=sp.getoutput('which python3'),
        help='python path you use (default: which python3)'
    )
    return parser


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()

    main(args)
