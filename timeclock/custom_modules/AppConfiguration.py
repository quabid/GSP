import pickle
from .index import exists, is_file, CONSOLE_MESSENGER_SWITCH, SEP, LINE_SEP, CUR_DIR


def save_config(content, location="{}{}".format(CUR_DIR, SEP)):
    with open("{}timer_app_config.conf".format(location), "wb") as file:
        pickle.dump(content, file)
    file.close()


def get_config():
    configuration_file = None

    if exists('timer_app_config.conf') and is_file('timer_app_config.conf'):
        custom_message = CONSOLE_MESSENGER_SWITCH['custom']
        message = custom_message("Found Configuration File!", 190, 110, 189)
        print("{}\t\t{}".format(LINE_SEP, message))

        with open('timer_app_config.conf', 'rb') as config:
            configuration_file = pickle.load(config)
    else:
        function = CONSOLE_MESSENGER_SWITCH['warning']
        message = function('No Configuration File Found!')
        print("{}\t\t{}".format(LINE_SEP, message))
        return None

    return configuration_file


def handle_window_open(window, coordinates):
    x = coordinates['x']
    y = coordinates['y']
    window.geometry("+{}+{}".format(x, y))
