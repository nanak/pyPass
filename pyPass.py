'''
generates unique passwords that are easily reproducible

'''

from subprocess import call, Popen, PIPE
import hashlib


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
    s = u'' + prm
    senc = s.encode('utf-8')
    sha.update(senc)
    return sha.hexdigest()

prt = hashSHA1("Test")
print(prt)

# splited = str.partition('\n')
# print [splited[0]]
