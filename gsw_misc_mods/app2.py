#! /usr/bin/env python3
from custom_modules.index import custom, error, success, warning, strip_args, log, generate_password, BRK, DASH, LINE, TAB

DESC = 'calling this app with single keywords or multiple argument will perform some action'


def default():
    line = custom('program activated'.title(), 160, 186, 245)
    print("{}{}{}{}{}{}{}{}{}{}".format(
        BRK, TAB, TAB, TAB, TAB, line, BRK, LINE, BRK, BRK))


def usage():
    line = custom('usage'.title(), 186, 180, 110)
    print("{}{}:{}".format(BRK, line, BRK))


SWITCH = {
    "gpwd": generate_password,
    "default": default
}

hasArgs, U_ARGS, argLen = strip_args()

if hasArgs:
    if argLen == 1:
        command = U_ARGS[0]
        try:
            function = SWITCH[command]
            function()
        except KeyError:
            # err_msg = error("\n\tError:\n\t\tCommand {} not found\n".format(U_ARGS[0].upper()))
            # print("{}".format(err_msg))
            usage()
