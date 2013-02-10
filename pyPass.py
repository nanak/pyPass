'''
generates unique passwords that are easily reproducible

'''

from subprocess import call, Popen, PIPE
import hashlib
import getpass


def getUUID():
    uuid1 = call(["powershell", "get-wmiobject Win32_ComputerSystemProduct |\
        Select-Object -ExpandProperty UUID"])

    uuid2 = Popen(["powershell", "get-wmiobject Win32_ComputerSystemProduct |\
        Select-Object -ExpandProperty UUID"], stdout=PIPE)

    output = uuid2.stdout.read()
    # splited1 = output.partition('\'')
    # splited2 = splited1.partition('\n')

    print("Test")
    print(uuid1)
    print(uuid2)
    print(output)


def hashSHA1(prm):
    sha = hashlib.sha1()
    s = prm
    senc = s.encode('utf-8')
    sha.update(senc)
    return sha.hexdigest()


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

# splited = str.partition('\n')
# print [splited[0]]
