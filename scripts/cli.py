import argparse

from .build import build


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    build(args.debug)
