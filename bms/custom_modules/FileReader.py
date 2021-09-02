from pathlib import Path


# Returns the lines contain in given file path
# @params file: Absolute or relative file path
# @returns
def return_lines(file):
    return file.readlines()


# Returns the lines contain in given file path
# @params file: Absolute or relative file path
# @returns file's text
def return_text(file):
    if type(file) == str:
        return Path(file).read_text()


# Returns the lines contain in given file path
# @params file: Absolute or relative file path
# @returns file's bytes
def return_bytes(file):
    if type(file) == str:
        return Path(file).read_bytes()
