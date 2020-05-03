#!/usr/bin/python3
import sys


# def readinput(argv=None):
if (len(sys.argv)) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

if sys.argv[1] != "README.md":
    print("Missing README.md", file=sys.stderr)
    exit(1)

exit(0)
