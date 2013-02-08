'''
generates a password based on UUID, ...

'''

from subprocess import call, Popen, PIPE


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


def hashSHA1():
    import hashlib
    h = hashlib.sha1()
    s = u'Test'
    h.update(s)
    senc = s.encode('utf-8')
    h.update(senc)
    print(h.hexdigest())

hashSHA1()

# splited = str.partition('\n')
# print [splited[0]]
