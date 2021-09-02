from tkinter import simpledialog
import os
from .FileValidator import isDir


def set_file_name():
    file_name = simpledialog.askstring(
        title="File Name", prompt="What should the file's name be?:")
    if None == file_name:
        return
    return file_name


def set_ext_name():
    ext_name = simpledialog.askstring(title="File's Extension",
                                      prompt="What should the file's extension be?:")
    if None == ext_name:
        return
    return ext_name


def set_save_destination():
    dest_path = simpledialog.askstring(title="Save Destination",
                                       prompt="Where should I save the file?:")
    if None == dest_path:
        return
    if not dest_path.rfind(os.sep):
        dest_path = "{}{}".format(dest_path, os.sep)
    return dest_path


def save_content_to_file_requirements():
    file_name = None
    ext_name = None
    dest_path = ''

    if not file_name:
        file_name = set_file_name()
        if None == file_name:
            return None

    if not ext_name:
        ext_name = set_ext_name()
        if None == ext_name:
            return None

    if not isDir(dest_path) or not dest_path:
        dest_path = set_save_destination()
        if None == dest_path:
            return None

    return "{}{}{}{}".format(dest_path, os.sep, file_name, ext_name)
