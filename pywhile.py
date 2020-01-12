#!/usr/local/bin/python3
from sys import argv, stdin
import subprocess as sp
from multiprocessing import Pool

__doc__ = """
Usage:
    pywhile COMMAND
    pywhile [-h | --help]

Options:
    -h --help     Show this screen and exit.
    -p --parallel Run parallel

Note:
    COMMADN 標準入力を次々と実行
    ex)
        ls | pywhile rm
        ls | pywhile rm -r
        ls | pywhile "python script.py #f"
        ls | pywhile "python script.py #f" -p
"""

PARALLEL = False

def usage():
    print(__doc__)
    exit()


def gen_command(com, line):
    # com: list -> str
    command = ' '.join(com)
    if "#f" in command:
        command = command.replace('#f', line.strip(), -1)
    else:
        command = command + ' ' + line.strip()
    # com: str -> list
    command = command.split()
    return command


def main(com):
    if not PARALLEL:
        for line in stdin.readlines():
            sp.run(gen_command(com, line))
    else:
        commands = [gen_command(com, line) for line in stdin.readlines()]
        with Pool(processes=None) as pool:
            pool.map(sp.run, commands)


if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
        if v in ['-p', '--parallel']:
            PARALLEL = True
            argv.remove(v)
    if len(argv) != 1:
        main(com=argv[1:])
    else:
        usage()
