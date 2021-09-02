import os
import re

p_ext = re.compile(".*(\\.[a-z]+)$")


def exists(filePath):
    return os.path.exists(filePath)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def is_symLink(path):
    return os.path.islink(path)


def has_extension(path):
    return p_ext.search(path) != None
