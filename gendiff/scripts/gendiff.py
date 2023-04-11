#!usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import display_help


def main():
    one_path, two_path = display_help()
    diff = generate_diff(one_path, two_path)
    print(diff)


if __name__ == "__main__":
    main()
