
from os import error


def readFileToConsole(file):
    try:
        lines = file.readlines()
        for l in lines:
            print(l)
    except:
        print("\n\tError reading {}\n\n".format(file.name))
