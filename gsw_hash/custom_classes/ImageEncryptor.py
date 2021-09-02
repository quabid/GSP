from custom_modules.index import exists, CONSOLE_MESSENGER_SWITCH as cms
from custom_classes.index import Hasher
from pathlib import PurePath, Path


class ImageEncryptor:
    __hasher = Hasher()

    def __init__(this):
        this.image_path = None
        this.hash_key = None
        this.image_read = None
        this.image_bytearray = None
        this.hashed_key = None

    def set_image_path(this, path):
        if type(path) == str:

            if not exists(path):

                print('File {} does not exist'.format(path))

                return {
                    'status': False,
                    'cause': 'File {} does not exist'.format(path)
                }

            else:
                this.image_path = path

                return {'status': True}

        elif isinstance(path, PurePath):

            if not exists(path._flavour.pathmod.abspath(path)):

                print('File {} does not exist'.format(
                    path._flavour.pathmod.abspath(path)))

                return {
                    'status':
                    False,
                    'cause':
                    'File {} does not exist'.format(
                        path._flavour.pathmod.abspath(path))
                }

            else:

                this.image_path = path._flavour.pathmod.abspath(path)

                return {'status': True}

    def encrypt(this):
        hash_results = this.__hasher.hash_data(this.image_path, '3_512')

        if hash_results['status']:
            this.hash_key = hash_results['hashed']

            try:
                fin = open(this.image_path, 'rb')

                this.image_read = fin.read()

                fin.close()

                this.image_bytearray = bytearray(this.image_read)

                this.hashed_key = (hash(this.hash_key) % 2)

                # performing XOR operation on each value of bytearray
                for index, values in enumerate(this.image_bytearray):
                    this.image_bytearray[index] = values ^ this.hashed_key

                fin = open(this.image_path, 'wb')

                fin.write(this.image_bytearray)

                fin.close()

                function = cms['success']

                msg = function('Encrypted {} successfully'.format(
                    this.image_path))

                print('\n\t{}\n\n'.format(msg))

                return {'status': True, 'hashed key': this.hashed_key}

            except Exception as ex:
                function = cms['error']

                msg = cms['custom']

                error = function('Error encrypting file {}'.format(
                    this.image_path))

                cause = msg('Cause:\t{}'.format(ex))

                print('\n\t{}\n\t{}'.format(error, cause))

                return {'status': False, 'cause': ex}

        else:
            error = cms['error']

            error_msg = cms['custom']

            msg = error('Error creating hash key')

            cause = error_msg('Cause:\t{}'.format(hash_results['cause']))

            print('\n\t{}\n\t{}'.format(msg, cause))

            return {'status': False, 'cause': hash_results['cause']}

    def __str__(this):
        return 'Image Encryptor'
