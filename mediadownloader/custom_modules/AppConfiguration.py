import pickle
from .index import fileExists, isFile, CONSOLE_MESSENGER_SWITCH, SEP, LINE_SEP, CUR_DIR


def save_config(content, location="{}{}".format(CUR_DIR, SEP)):
    f = open("{}app_config.conf".format(location), "wb")
    pickle.dump(content, f)
    f.close()


def get_config():
    if fileExists('app_config.conf') and isFile('app_config.conf'):
        custom_message = CONSOLE_MESSENGER_SWITCH['custom']
        message = custom_message("Found Configuration File!", 190, 110, 189)
        print("{}\t\t{}".format(LINE_SEP, message))
        configuration_file = open('app_config.conf', 'rb')
        return pickle.load(configuration_file)
    else:
        function = CONSOLE_MESSENGER_SWITCH['warning']
        message = function('No Configuration File Found!')
        print("{}\t\t{}".format(LINE_SEP, message))
        return None


def handle_window_open(window, coordinates):
    x = coordinates['x']
    y = coordinates['y']
    window.geometry("+{}+{}".format(x, y))
