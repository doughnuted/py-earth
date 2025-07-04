import argparse
from timeit import default_timer as timer
import numpy as np
from pyearth._qr import Householder


def run(m, k, repeat):
    hh = Householder.alloc(m, k, 1e-12)
    x = np.zeros(m)
    start = timer()
    for i in range(repeat):
        x[:] = np.random.randn(m)
        hh.update_from_column(x)
    end = timer()
    return (end - start) / repeat


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, default=200)
    parser.add_argument("--k", type=int, default=100)
    parser.add_argument("--repeat", type=int, default=100)
    args = parser.parse_args()
    t = run(args.m, args.k, args.repeat)
    print(f"Average update time: {t:.6f}s")


if __name__ == "__main__":
    main()
