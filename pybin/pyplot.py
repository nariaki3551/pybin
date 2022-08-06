import argparse
import sys
import matplotlib.pyplot as plt


def main(title, xlabel, ylabel, xscale, yscale, marker, grid, savename):
    data = [list(map(float, row.split())) for row in sys.stdin.readlines()]
    fig, ax = plt.subplots()
    X = [d[0] for d in data]
    Y = [d[1] for d in data]
    ax.plot(X, Y, marker=marker)
    axtwinx = ax.twinx()
    for y_ix in range(len(data[0]) - 2):
        Y = [d[y_ix + 2] for d in data]
        axtwinx.plot(X, Y, marker=marker)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    if grid:
        ax.grid("--")
    if savename is not None:
        fig.savefig(savename)
    else:
        plt.show()


def cli_main():
    parser = argparse.ArgumentParser(description="create plot")
    parser.add_argument("--xlabel", default=None)
    parser.add_argument("--ylabel", default=None)
    parser.add_argument("--title", default=None)
    parser.add_argument("--xscale", choices=["linear", "log"], default="linear")
    parser.add_argument("--yscale", choices=["linear", "log"], default="linear")
    parser.add_argument("-m", "--marker", default="o")
    parser.add_argument("-g", "--grid", action="store_true")
    parser.add_argument("--savename", default=None)
    args = parser.parse_args()

    main(
        args.title,
        args.xlabel,
        args.ylabel,
        args.xscale,
        args.yscale,
        args.marker,
        args.grid,
        args.savename,
    )
