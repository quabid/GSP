from cryptography.fernet import Fernet as key_generator
from custom_modules.FileWriter import write_file


class CryptoKeyGenerator:
    def __init__(this):
        super().__init__()
        this.generated_key = None

    def generate_key(this, name='generated_key.key'):
        this.generated_key = key_generator.generate_key()

        # string the key in a file
        with open(name, 'wb') as filekey:
            filekey.write(this.generated_key)

        return {'status': True, 'key': this.generate_key}

    def __str__(this):
        return 'CryptoKeyGenerator'
