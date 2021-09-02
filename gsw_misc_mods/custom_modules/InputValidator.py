import re

pLetters = re.compile("^[a-zA-Z]+$")
pNumbers = re.compile("^[0-9]+$")
pEmail = re.compile(
    '^([a-zA-Z0-9]+)(\\.[a-zA-Z0-9]+)?@([a-zA-Z]+)\\.[a-zA-Z]{2,3}$')
pPasswordCharacterCriteria = re.compile("^[a-zA-Z0-9@#\$%\&]{6}$")


def isPasswordValidLength(arg): return len(arg) >= 6


def isString(arg): return (type(arg) == str and len(arg) > 0)


def isLetters(arg):
    return (type(arg) == str and len(arg) > 0 and pLetters.search(arg))


def isNumbers(arg):
    return ((type(arg) == int or type(arg) == float) and pNumbers.search(arg))


def isEmail(arg): return pEmail.search(arg)


def isPasswordValid(arg): return pPasswordCharacterCriteria.search(arg)
