import os


def log(arg):
    msg = "\n{0}\n"
    print(msg.format(str(arg)))


def cls(): os.system('clear')
