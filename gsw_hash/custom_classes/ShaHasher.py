from hashlib import sha384, sha256, sha224, sha3_224, sha3_256, sha3_384, sha3_512
from .AvailabilityFinder import AvailabilityFinder as AF
from custom_modules.FileWriter import write_file

# hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()


class Hasher:
    def __init__(this):
        this.ShaSwitch = {
            'sha224': sha224,
            'sha256': sha256,
            'sha384': sha384,
            'sha3_224': sha3_224,
            'sha3_256': sha3_256,
            'sha3_384': sha3_384,
            'sha3_512': sha3_512
        }
        this.af = AF()

    def hash_data(this, data, scheme, verbose=False):
        hash = None

        if not type(scheme) == str:
            scheme = str(scheme)

        if not scheme.startswith('sha'):
            scheme = "{}{}".format("sha", scheme)

        if not this.af.is_available(scheme):
            print("Scheme {} is not available on this system\n".format(scheme))
            return {
                'status':
                False,
                'cause':
                "Scheme {} is not available on this system\n".format(scheme)
            }

        try:
            hash_function = this.ShaSwitch[scheme]
            hash = hash_function(str(data).encode("utf-8")).hexdigest()

            if verbose:
                print(
                    "\n\tData:\t{}\n\tData Type:\t{}\n\tScheme:\t{}\n\tGenerated Hash:\t{}"
                    .format(data, type(data), scheme, hash))

            return {'status': True, 'hashed': hash}
        except TypeError as te:
            print("Type Error:\t{}".format(te))
            return {'status': False, 'cause': te}
        except KeyError as ke:
            print("Key Error:\t{}".format(ke))
            return {'status': False, 'cause': ke}
        except LookupError as le:
            print("Lookup Error:\t{}".format(le))
            return {'status': False, 'cause': le}

    def hash_data_to_file(this,
                          data,
                          scheme,
                          name="hashkey.txt",
                          verbose=False):
        hash = None

        if not type(scheme) == str:
            scheme = str(scheme)

        if not scheme.startswith('sha'):
            scheme = "{}{}".format("sha", scheme)

        if not this.af.is_available(scheme):
            print("Scheme {} is not available on this system\n".format(scheme))
            return {
                'status':
                False,
                'cause':
                "Scheme {} is not available on this system\n".format(scheme)
            }

        try:
            hash_function = this.ShaSwitch[scheme]
            hash = hash_function(str(data).encode("utf-8")).hexdigest()

            if verbose:
                print(
                    "\n\tData:\t{}\n\tData Type:\t{}\n\tScheme:\t{}\n\tGenerated Hash:\t{}"
                    .format(data, type(data), scheme, hash))
            write_file(name, hash)
            return {'status': True, 'hashed': hash}
        except TypeError as te:
            print("Type Error:\t{}".format(te))
            return {'status': False, 'cause': te}
        except KeyError as ke:
            print("Key Error:\t{}".format(ke))
            return {'status': False, 'cause': ke}
