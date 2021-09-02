import os


def exists(filePath):
    return os.path.exists(filePath)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def is_sym_Link(path):
    return os.path.islink(path)