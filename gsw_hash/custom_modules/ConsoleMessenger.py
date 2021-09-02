from sty import fg, ef, rs, Style, RgbFg, bg, RgbBg
# from colorama import Fore, Style


"""  last = fg.magenta + ef.italic + ef.bold + "Last Arg: " + U_ARGS[(len(U_ARGS) - 1)] + rs.all
first = fg.cyan + ef.italic + ef.bold + "First Arg: " + U_ARGS[0] + rs.all
msg = fg.red + ef.italic + ef.bold + "No Arguments" + rs.all """


def error(arg):
    line = ""
    size = 0

    if (arg.find(" ") > 0):
        spaceSplit = arg.split(" ")
        line = fg.red + ef.italic + ef.bold
        size = len(spaceSplit) - 1

        for i, s in enumerate(spaceSplit):
            if i < size:
                line += s + " "
            else:
                line += s

    elif (arg.find("-") > 0):
        dashSplit = arg.split("-")
        line = fg.red + ef.italic + ef.bold
        size = len(dashSplit) - 1

        for i, e in enumerate(dashSplit):
            if i < size:
                line += e + " "
            else:
                line += e

    elif (arg.find("_") > 0):
        underscoreSplit = arg.split("_")
        line = fg.red + ef.italic + ef.bold
        size = len(underscoreSplit) - 1

        for i, u in enumerate(underscoreSplit):
            if i < size:
                line += u + " "
            else:
                line += u

    else:
        line = fg.red + ef.italic + ef.bold + arg

    line += rs.all

    return line


def warning(arg):
    line = ""
    size = 0

    if (arg.find(" ") > 0):
        spaceSplit = arg.split(" ")
        line = fg.yellow + ef.italic + ef.bold
        size = len(spaceSplit) - 1

        for i, s in enumerate(spaceSplit):
            if i < size:
                line += s + " "
            else:
                line += s

    elif (arg.find("-") > 0):
        dashSplit = arg.split("-")
        line = fg.yellow + ef.italic + ef.bold
        size = len(dashSplit) - 1

        for i, e in enumerate(dashSplit):
            if i < size:
                line += e + " "
            else:
                line += e

    elif (arg.find("_") > 0):
        underscoreSplit = arg.split("_")
        line = fg.yellow + ef.italic + ef.bold
        size = len(underscoreSplit) - 1

        for i, u in enumerate(underscoreSplit):
            if i < size:
                line += u + " "
            else:
                line += u

    else:
        line = fg.yellow + ef.italic + ef.bold + arg

    line += rs.all

    return line


def success(arg):
    line = ""
    size = 0

    if (arg.find(" ") > 0):
        spaceSplit = arg.split(" ")
        line = fg.green + ef.italic + ef.bold
        size = len(spaceSplit) - 1

        for i, s in enumerate(spaceSplit):
            if i < size:
                line += s + " "
            else:
                line += s

    elif (arg.find("-") > 0):
        dashSplit = arg.split("-")
        line = fg.green + ef.italic + ef.bold
        size = len(dashSplit) - 1

        for i, e in enumerate(dashSplit):
            if i < size:
                line += e + " "
            else:
                line += e

    elif (arg.find("_") > 0):
        underscoreSplit = arg.split("_")
        line = fg.green + ef.italic + ef.bold
        size = len(underscoreSplit) - 1

        for i, u in enumerate(underscoreSplit):
            if i < size:
                line += u + " "
            else:
                line += u

    else:
        line = fg.green + ef.italic + ef.bold + arg

    line += rs.all

    return line


def custom(arg, r=239, g=220, b=197):
    line = ""
    size = 0

    if (arg.find(" ") > 0):
        spaceSplit = arg.split(" ")
        line = fg(r, g, b) + ef.italic + ef.bold
        size = len(spaceSplit) - 1

        for i, s in enumerate(spaceSplit):
            if i < size:
                line += s + " "
            else:
                line += s

    elif (arg.find("-") > 0):
        dashSplit = arg.split("-")
        line = fg(r, g, b) + ef.italic + ef.bold
        size = len(dashSplit) - 1

        for i, e in enumerate(dashSplit):
            if i < size:
                line += e + " "
            else:
                line += e

    elif (arg.find("_") > 0):
        underscoreSplit = arg.split("_")
        line = fg(r, g, b) + ef.italic + ef.bold
        size = len(underscoreSplit) - 1

        for i, u in enumerate(underscoreSplit):
            if i < size:
                line += u + " "
            else:
                line += u

    else:
        line = fg(r, g, b) + ef.italic + ef.bold + arg

    line += rs.all

    return line


CONSOLE_MESSENGER_SWITCH = {
    "error": error,
    "warning": warning,
    "success": success,
    "custom": custom
}
