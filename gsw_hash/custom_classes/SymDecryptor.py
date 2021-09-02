from cryptography.fernet import Fernet
from custom_modules.FileValidator import exists, is_file, is_symLink
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


class SymDecryptor:
    def __init__(this):
        this.decrypted_file = None
        this.encryption_key = None
        this.data_file = None

    def decrypt(this, key_file, data_file):
        if not exists(key_file):
            function = cms['error']
            msg = function('Key file {} does not exist\n'.format(key_file))
            print(msg)
            return {
                'status':
                False,
                'cause':
                'Key file {} does not exist\nThis program requires an encrypted key\n\n'
                .format(key_file)
            }

        elif not exists(data_file):
            function = cms['error']
            msg = function(
                'The data file {} does not exist\n'.format(data_file))
            print(msg)
            return {
                'status':
                False,
                'cause':
                'Data file {} does not exist\nThis program requires a file to encrypt\n\n'
                .format(key_file)
            }

        elif not is_file(data_file):
            function = cms['error']
            msg = function(
                'The data file {} is not a valid file\n'.format(data_file))
            print(msg)
            return {
                'status':
                False,
                'cause':
                'Data file {} must be a regular file\n\n'.format(data_file)
            }

        elif not is_file(key_file):
            function = cms['error']
            msg = function(
                'The key file {} is not a valid file\n'.format(key_file))
            print(msg)
            return {
                'status': False,
                'cause':
                'Key file {} must be a regular file\n\n'.format(key_file)
            }

        elif is_symLink(key_file):
            function = cms['error']
            msg = function(
                'The key file {} must not be a symbolic link file\n'.format(
                    key_file))
            print(msg)
            return {
                'status': False,
                'cause':
                'Key file {} must be a regular file\n\n'.format(key_file)
            }

        elif is_symLink(data_file):
            function = cms['error']
            msg = function(
                'The data file {} must not be a symbolic link file\n'.format(
                    data_file))
            print(msg)
            return {
                'status':
                False,
                'cause':
                'Data file {} must be a regular file\n\n'.format(data_file)
            }

        # opening the key
        with open(key_file, 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(data_file, 'rb') as enc_file:
            encrypted = enc_file.read()

        # encrypting the file
        decrypted = fernet.decrypt(encrypted)
        this.decrypted_file = decrypted
        this.encryption_key = key_file
        this.data_file = data_file

        # opening the file in write mode and
        # writing the encrypted data
        with open(data_file, 'wb') as dec_file:
            dec_file.write(decrypted)

        return {'status': True}

    def write_decrypted_file(this):
        with open(this.data_file, 'wb') as dec_file:
            dec_file.write(this.decrypted_file)
        return {'status': True}
