from cryptography.fernet import Fernet
from custom_modules.FileValidator import exists, is_file, is_symLink
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


class SymEncryptor:
    def __init__(this):
        this.encrypted_file = None
        this.key_file = None
        this.data_file = None

    def encrypt(this, key_file, data_file):
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
        with open(data_file, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)
        this.encrypted_file = encrypted
        this.key_file = filekey
        this.data_file = data_file

        # opening the file in write mode and
        # writing the encrypted data
        with open(data_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        return {'status': True}

    def set_files(this, key_file, data_file):
        if not file_exists(key_file):
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

        elif not file_exists(data_file):
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

        this.data_file = data_file
        this.key_file = key_file

        return {'status': True}

    def write_encrypted_file(this):
        with open(this.key_file, 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(this.data_file, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(this.data_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        return {'status': True}

    def get_encrypted_file(this):
        return this.encrypted_file

    def get_key_file(this):
        return this.key_file

    def get_data_file(this):
        return this.data_file
