#!/usr/bin/python3

"""
This module converts markdown to html
"""


if __name__ == "__main__":
    from sys import argv, stderr
    from os import path
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    if not path.exists(argv[1]):
        print("Missing {}".format(argv[1]), file=stderr)
        # print("Missing README.md", file=stderr)
        exit(1)

    with open(argv[1]) as f:
        with open(argv[2], "w") as f1:
            for line in f:
                words = line.split()
                hnum = len(words[0])
                hopen = "<h" + str(hnum) + ">"
                hend = "</h" + str(hnum) + ">"
                newline = hopen
                for i in range(1, len(words)):
                    newline += words[i]
                    if i != len(words) - 1:
                        newline += " "
                newline += hend + "\n"
                print(newline)
                f1.write(newline)
