#!/usr/bin/python3
from sys import argv, stderr


# def readinput(argv=None):
if (len(argv)) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=stderr)
    exit (1)

if argv[1] != "README.md":
    print("Missing README.md", file=stderr)
    exit (1)

exit (0)
