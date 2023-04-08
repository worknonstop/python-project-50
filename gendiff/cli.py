#!usr/bin/env python3

import argparse


def display_help():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=argparse.FileType("r"))
    parser.add_argument("second_file", type=argparse.FileType("r"))

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == "__main__":
    display_help()
