import argparse
import sys
import matplotlib.pyplot as plt


def main(num_bins, title, xlabel, ylabel, xscale, yscale, savename):
    data = [float(row.strip()) for row in sys.stdin.readlines()]
    fig, ax = plt.subplots()
    ax.hist(data, num_bins)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    if savename is not None:
        fig.savefig(savename)
    else:
        plt.show()


def cli_main():
    parser = argparse.ArgumentParser(description="create histgram")
    parser.add_argument("-n", "--num_bins", type=int, help="number of bins of histgram")
    parser.add_argument("--xlabel", default=None)
    parser.add_argument("--ylabel", default=None)
    parser.add_argument("--title", default=None)
    parser.add_argument("--xscale", choices=["linear", "log"], default="linear")
    parser.add_argument("--yscale", choices=["linear", "log"], default="linear")
    parser.add_argument("--savename", default=None)
    args = parser.parse_args()

    main(
        args.num_bins,
        args.title,
        args.xlabel,
        args.ylabel,
        args.xscale,
        args.yscale,
        args.savename,
    )
