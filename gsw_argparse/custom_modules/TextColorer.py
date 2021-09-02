from sty import fg, ef, rs, Style, RgbFg, bg, RgbBg
from colorama import Fore, Style


"""  last = fg.magenta + ef.italic + ef.bold + "Last Arg: " + U_ARGS[(len(U_ARGS) - 1)] + rs.all
first = fg.cyan + ef.italic + ef.bold + "First Arg: " + U_ARGS[0] + rs.all
msg = fg.red + ef.italic + ef.bold + "No Arguments" + rs.all """


def color(arg, r=100, g=110, b=120):
    print("{}".format(fg(r, g, b) + arg + rs.all))
