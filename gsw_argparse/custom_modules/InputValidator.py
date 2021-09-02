import re

pattern = "^[a-zA-Z]+$"


def isString(arg):
    if (type(arg) == str and len(arg) > 0):
        return True
    else:
        return False


def isLetters(arg):
    if (type(arg) == str and len(arg) > 0 and re.search(pattern, arg)):
        return True
    else:
        return False
