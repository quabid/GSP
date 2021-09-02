#! /usr/bin/env python3

import sys
import re
import os

num_pattern = re.compile("^[0-9.]+$")
letter_pattern = re.compile("^[a-zA-Z]+$")
punctuatin_pattern = re.compile("^[\\.\\,\\?\\!\\;\\:]+$")


def get_args():
    args = sys.argv
    args_size = len(args[1:])

    if len(args) > 1:
        return True, args[1:], args_size
    else:
        return False, None, 0


def date_suffix(num=None):
    number = ""

    SWITCH = {
        "1": "st",
        "2": "nd",
        "3": "rd",
        "4": "th",
        "5": "th",
        "6": "th",
        "7": "th",
        "8": "th",
        "9": "th",
        "0": "th"
    }

    if None != num:

        if type(num) == int or type(num) == float:
            number = str(int(num))
        else:
            number = num

        if num_pattern.search(number):
            if number[-2:] == "11":
                return True, number + 'th'

            last_index = number[-1:]
            return True, number + SWITCH[last_index]
        else:
            return False, None


def is_number(arg):
    if num_pattern.search(arg):
        return True
    else:
        return False


def is_letter(arg):
    if letter_pattern.search(arg):
        return True
    else:
        return False


def is_punctuation(arg):
    if punctuatin_pattern.search(arg):
        return True
    else:
        return False


def cls():
    os.system('clear')
