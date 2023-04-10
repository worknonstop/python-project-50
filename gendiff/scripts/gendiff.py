#!usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import display_help


def main():
    display_help()
    diff = generate_diff("gendiff/file1.json", "gendiff/file2.json")
    print(diff)


if __name__ == "__main__":
    main()
