#!/usr/bin/python3
"""
    0-read_file
    Reads a text file (UTF8) and prints it to stdout
"""


def append_after(filename="", search_string="", new_string=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    text = ""
    with open(filename, mode="r", encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(text)
