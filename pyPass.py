'''
generates unique passwords that are easily reproducible

'''

import hashlib
import getpass
import base64


def hashSHA1(prm):
    # return hashlib.sha1(prm.encode('utf-8')).hexdigest()
    # base64 expects bytes, not hex
    return hashlib.sha1(prm.encode('utf-8')).digest()


def inp():
    keyw = str(input("Enter Keyword: "))
    while 1:
        print("Enter Master Password")
        master1 = str(getpass.getpass())
        print("Enter Master Password again")
        master2 = str(getpass.getpass())
        if master1 == master2:
            key_and_master = keyw + master1
            break
        else:
            print("Passwords did not match, try again")
            pass
    return key_and_master

passw = hashSHA1(inp())
print(passw)
# Test of base 64 encoded password
passw2 = base64.standard_b64encode(passw)
print(passw2)

# splited = str.partition('\n')
# print [splited[0]]
