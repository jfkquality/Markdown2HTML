#!/usr/bin/python3
"""Check for markdown file."""

from __future__ import print_function
import sys


def getinput(*args):
    """ Parse input and test."""
    myargs = args[0]
    if len(myargs) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if myargs[1] != "README.md":
        print("Missing README.md", file=sys.stderr)
        exit(1)
    exit(0)


if __name__ == "__main__":
    getinput(sys.argv)
