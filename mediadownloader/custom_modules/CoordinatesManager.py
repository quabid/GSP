import pickle
from .FileValidator import fileExists, isFile
from .ConsoleMessenger import error, success, warning, custom


def save_location(grid_location):
    location_file = open('coordinates.ser', 'wb')
    pickle.dump(grid_location, location_file)
    location_file.close()


def get_location():
    if fileExists('coordinates.ser'):
        message = custom("Woo Hoo!", 190, 100, 188)
        print("\t\t{}\n\n".format(message))
        location_file = open('coordinates.ser', 'rb')
        location_coordinates = pickle.load(location_file)
        return location_coordinates
    else:
        message = error("Doh!")
        print("\t\t{}\n".format(message))
        return None
