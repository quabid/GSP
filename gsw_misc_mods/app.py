#! /usr/bin/env python3
from custom_modules.log import log
from custom_modules.utils import clear
from custom_modules.hasher import hash_password, check_password
from custom_modules.jwt import generate_token, get_info, get_meta, refresh_token, verify_token


def init():
    print('\n\tHuh?\n\t\t{}\n\n'.format('camera man'.capitalize()))


init()
