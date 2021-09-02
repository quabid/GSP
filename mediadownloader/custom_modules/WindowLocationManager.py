from .CoordinatesManager import save_location, get_location
from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH


def window_location_handler(window):

    def on_close():
        message = CONSOLE_MESSENGER_SWITCH['warning'](
            'Closing the main window')
        print("\n\t\t{}\n".format(message))
        coordinates = {
            'x': window.winfo_rootx(),
            'y': window.winfo_rooty()
        }
        save_location(coordinates)
        window.destroy()

    def on_open(content):
        message = CONSOLE_MESSENGER_SWITCH['success']('Opening the main window')
        print("\n\t\t{}\n".format(message))
        win_coordinates = get_location()
        x = None
        y = None
        if win_coordinates:
            x = win_coordinates['x']
            y = win_coordinates['y']
            content.geometry("+{}+{}".format(x, y))

    window.protocol("WM_DELETE_WINDOW", on_close)
    on_open(window)
