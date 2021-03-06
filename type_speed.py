#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

"""
Lets the user type something and calculates the typing speed.
"""

import argparse
import datetime

__docformat__ = "restructuredtext en"

def main():
    options = _parse_args()

    start = datetime.datetime.now()

    text = input("Type!\n")

    end = datetime.datetime.now()
    diff = end-start
    chars = len(text)
    time = diff.seconds

    try:
        speed = chars/time
    except ZeroDivisionError:
        print("That was too short, please type more than a second.")
    else:
        print("You typed {chars:n} chars in {seconds:n} seconds. That is {speed:.1f} chars/second or {min:.1f} chars/minute. And {words:.1f} words per minute.".format(
            chars=chars,
            seconds=time,
            speed=speed,
            min=speed * 60,
            words=len(text.split())/time*60.0
        ))

def _parse_args():
    """
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    """
    parser = argparse.ArgumentParser(description=__doc__)

    return parser.parse_args()

if __name__ == "__main__":
    main()
