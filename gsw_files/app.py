#! /usr/bin/env python3
import sys
from custom_modules.Utils import log
from custom_modules.index import fileExists, isDir, isFile, isSymLink, getFile, readFileToConsole

ARGS = sys.argv
ARGS_COUNT = len(ARGS)
SWITCH = {
    "exists": lambda path: fileExists(path),
    "isfile": lambda path: isFile(path),
    "isdir": lambda path: isDir(path),
    "issymlink": lambda path: isSymLink(path),
    "getfile": lambda path: getFile(path)
}

if ARGS_COUNT > 1:
    if ARGS_COUNT == 3:
        if ARGS[2] == "exists" or ARGS[2] == "isfile" or ARGS[2] == "isdir" or ARGS[2] == "issymlink":
            filePath = ARGS[1]
            if fileExists(filePath):
                if isFile(filePath):
                    function = SWITCH[ARGS[2]]
                    results = function(filePath)
                    log("\n\tPath {0} {1} {2}\n\n".format(
                        ARGS[1], ARGS[2], results))
                else:
                    log("\n\t{0} is not a file\n\n".format(filePath))
            else:
                log("\n\tFile path {0} does not exists\n\n".format(filePath))
        elif ARGS[2] == "getfile":
            function = SWITCH[ARGS[2]]
            filePath = ARGS[1]
            if fileExists(filePath):
                if isFile(filePath):
                    file = function(filePath)
                    readFileToConsole(file)
                else:
                    log("\n\t{0} is not a file\n\n".format(filePath))
            else:
                log("\n\t File path {0} does not exist\n\n".format(filePath))
        else:
            log(
                "\n\tError: Must enter one of the following valid action keys as the last parameter - keys: {0}\n\tYou entered: {1}".format(SWITCH.keys(), ARGS[2]))
else:
    log("\n\t{0}\n".format("No arguments"))
