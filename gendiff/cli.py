#!usr/bin/env python3

import argparse


def display_help():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f", "--format", type=str, default="json", help="set format of output"
    )
    args = parser.parse_args()
    return args.first_file, args.second_file


if __name__ == "__main__":
    display_help()
