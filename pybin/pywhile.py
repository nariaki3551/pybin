import argparse
import sys
import subprocess
import multiprocessing
import tqdm

EXAMPLE = """
ex)
    ls | pywhile rm
    ls | pywhile rm -r
    ls | pywhile "python script.py #f"
    ls | pywhile "python script.py #f" -p 2
"""


def gen_command_data(command, line):
    if "." == command:
        command = line.strip()
    elif "#f" in command:
        command = command.replace("#f", line.strip(), -1)
    else:
        command = command + " " + line.strip()
    # com: str -> list
    command = command.split()
    # redirect
    if ">" in command:
        output_file = command[command.index(">") + 1]
        command = command[: command.index(">")]
    else:
        output_file = None
    return command, output_file


def run(command_data, quiet):
    command, output_file = command_data

    if not quiet:
        if output_file is not None:
            print(" ".join(command), ">", output_file)
        else:
            print(" ".join(command))

    if output_file is not None:
        stdout = open(output_file, "w")
    else:
        stdout = subprocess.STDOUT
        stdout = None

    proc = subprocess.Popen(command, stdout=stdout)
    proc.wait()


def main(command, num_processes, quiet, progress, chunksize):
    if progress:
        iter_wrapper = tqdm.tqdm
    else:
        iter_wrapper = lambda x, *args, **kwargs: x

    if num_processes == 1:
        lines = list(sys.stdin.readlines())
        for line in iter_wrapper(lines):
            run(gen_command_data(command, line))
    else:
        commands = [gen_command_data(command, line) for line in sys.stdin.readlines()]
        with multiprocessing.Pool(processes=num_processes) as pool:
            args = [(command, quiet) for command in commands]
            imap = pool.imap(run, args, chunksize=chunksize)
            list(iter_wrapper(imap, total=len(commands)))


def cli_main():
    parser = argparse.ArgumentParser(
        description="run command + input",
    )
    parser.add_argument(
        "command",
        help="command "
        + "- #f is replaced to stdin;"
        + "- if it is ., then run stdin as command",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="do not display command"
    )
    parser.add_argument(
        "-p",
        "--num_processes",
        type=int,
        default=1,
        help="process number when parallel execution",
    )
    parser.add_argument(
        "-c",
        "--chunksize",
        type=int,
        default=1,
        help="chunksize of imap",
    )
    parser.add_argument(
        "--progress",
        action="store_true",
        help="show progress",
    )
    args = parser.parse_args()

    main(args.command, args.num_processes, args.quiet, args.progress, args.chunksize)
