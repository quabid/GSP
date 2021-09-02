import re

# Number types
integer_pattern = re.compile('^[0-9]+$')
float_pattern = re.compile('^[0-9]+(\\.[0-9]+){1}$')

# Alphabet characters
string_pattern = re.compile('^[a-zA-Z]+$')

# Punctations
punctuation_pattern = re.compile("^[\\.\\,\\?\\!\\;\\:]+$")
