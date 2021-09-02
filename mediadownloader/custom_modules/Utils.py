import os
import types


def cls(): return os.system('clear')


def bind_event(target, event, method):
    if type(target) != None and type(event) == str and type(method) == types.MethodType:
        target.bind("<{}>".format(event), method)


def print_to_console(arg):
    print(f"{arg}")


be = bind_event
ptc = print_to_console


SERVER_BASE = {
    "syoutube": "https://www.youtube.com",
    "oyoutube": "http://www.youtube.com",
    "syt": "https://wwww.youtube.com",
    "oyt": "http://www.youtube.com"
}
