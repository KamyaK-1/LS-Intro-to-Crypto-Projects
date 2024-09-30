def encrypt(cipher,key):
    ans = ""
    for character in cipher:
        if character == ' ':
            ans = ans + character
        else:
            ans = ans + chr((ord(character)-39+key)%26+65)
    return ans
def decrypt(cipher,key):
    ans = ""
    for character in cipher:
        if character == ' ':
            ans = ans + character
        else:
            ans = ans + chr((ord(character)-39-key)%26+65)
    return ans
print(decrypt('HAAHJR HA KHDU',7))
print(decrypt( 'EVAT NEBHAQ GUR EBFVR',13))
print(encrypt( 'EVAT NEBHAQ GUR EBFVR',13))