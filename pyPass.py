#!/usr/bin/env python3
'''
generates unique passwords that are easily reproducible

'''

import hashlib
import getpass
import base64
import transcode as tran

DIGITS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-_@.:,;!"§$%&/()=?üöäÜÖÄ'


def hashSHA1(param):
	# hash parameter with sha1 to bytestring
	return hashlib.sha1(param.encode('utf-8')).hexdigest()


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
	return key_and_master

passw = hashSHA1(inp())
passw = tran.transcode(passw, DIGITS, tran.BASE16_DIGITS)
print(passw)
