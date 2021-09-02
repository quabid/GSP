from jet import JET
from jet.utils import hmac_sha256


GLOBAL_JET = JET(
    SECRET='ejt2Q71f6G___m20Z'
)

user_secret = hmac_sha256('user-password', 'user-password', 'ascii')

payload = {
    'id': 1,
    'message': "Hola"
}

# Generate token
# token = GLOBAL_JET.encrypt(user_secret, payload)


def generate_token(arg):
    return GLOBAL_JET.encrypt(user_secret, arg)

# Get info on token
# decrypted_meta, decrypted_payload = GLOBAL_JET.decrypt(user_secret, token)


def get_meta(token):
    return GLOBAL_JET.decrypt(user_secret, token)

# Get info on token without user_secret
# decrypted_meta, decrypted_payload = GLOBAL_JET.decrypt_from_PK(token)


def get_info(token):
    return GLOBAL_JET.decrypt_from_PK(token)


# Verify token
""" verified_sign = GLOBAL_JET.is_valid_token(token)
print("Token is valid? ", verified_sign) """


def verify_token(token):
    return GLOBAL_JET.is_valid_token(token)


# Refresh token
""" new_token = GLOBAL_JET.refresh_token(token)
print("Token == New Token ", token == new_token) """


def refresh_token(token):
    return GLOBAL_JET.refresh_token(token)
