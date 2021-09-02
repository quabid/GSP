from os import error


def read_file_to_console(file):
    try:
        lines = file.readlines()
        for l in lines:
            print(l)
    except:
        print("\n\tError reading {}\n\n".format(file.name))
