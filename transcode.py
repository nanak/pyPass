BASE64_DIGITS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

BASE16_DIGITS = '0123456789ABCDEF'

BASE2_DIGITS = '01'


# Decodes an encoded number into a decimal number.
#
# data ... the encoded number (string)
# source ... the system the number is encoded in (string)
def decode(data, source):
    value = 0
    for d in data:
        if d in source:
            value = value * len(source)
            value = value + source.find(d)
    return value


# Encodes a decimal number into system given by target
#
# data ...  number that should be encoded
# target ... system the number should be encoded to
def encode(data, target):
    result = ''
    while int(data) > 0:
        r = int(data % len(target))
        result = target[r] + result
        data = data / len(target)
    return result


# Transcodes a number from one numeric system to another.
# For examples to see how a 'system' should look like, take a
# look at the constants BASE64_DIGITS, BASE16_DIGITS (hexadecimal),
# string.digits (decimal), string.octdigits (octal)
# and BASE2_DIGITS (binary)
#
# Unsigned numbers only since the '-' character could also be
# used as a digit.
#
# All the parameters should be Strings!
#
# data ... number that should be transcoded
# target ... target system the number should be encoded to
# source ... system the number is currently encoded in
#
def transcode(data, target, source):
    return encode(decode(data, source), target)
