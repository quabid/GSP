from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from .FileValidator import has_extension
from .PlatformConstants import LINE_SEP

# This method creates a new or over-writes an existing file
# @param path: An absolute or relative file path
# @param mode: Optional file creationg mode - defaults to write
# @return: dict with status property True for success or False for failure


def write_file(path, data=None, mode='w'):
    if has_extension(path):
        f = open(path, mode)

        if data != None:
            if type(data) == dict:
                for d in data.values():
                    f.write("{}{}".format(d, LINE_SEP))
            else:
                f.writelines(data)

        f.close()

        function = cms['success']
        print(function("File {} successfully created!".format(path)))
        return {'status': True}
    else:
        function = cms['error']
        print(function("Unable to create file {}".format(path)))
        return {
            'status': False,
            'cause': 'File name must end with an extension'
        }
