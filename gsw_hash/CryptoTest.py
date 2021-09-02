from custom_classes.index import ShaHasher as Hasher, AvailabilityFinder as AF, CryptoKeyGenerator as Ckg, SymEncryptor as Symcryptor, SymDecryptor as SymDecryptor
from custom_modules.index import CONSOLE_MESSENGER_SWITCH as cms, sleep, read_file


def run_test():
    function = cms['custom']

    status = function('Printing the unencrypted data file')
    print(status)

    read_file('nba.csv')

    sleep()

    status = function('Instantiating the key generator')
    print(status)

    ckg = Ckg()

    sleep()

    status = function('Generating the crypto key')
    print(status)

    results = ckg.generate_key('generated_csv_key.key')

    sleep()

    status = function('Instantiating the symetric key generator')
    print(status)

    symcryptor = Symcryptor()

    sleep()

    status = function('Encrypting the data file')
    print(status)

    results = symcryptor.encrypt('generated_csv_key.key', 'nba.csv')

    sleep()

    status = function('Printing the encrypted data file')
    print(status)

    sleep()

    status = function('Printing the encrypted data file')
    print(status)

    read_file('nba.csv')

    sleep()

    status = function('Decrypting the encryped data file')
    print(status)

    symdecryptor = SymDecryptor()

    results = symdecryptor.decrypt('generated_csv_key.key', 'nba.csv')

    sleep()

    status = function('Printing the original unencrypted data file')
    print(status)

    sleep()

    read_file('nba.csv')
