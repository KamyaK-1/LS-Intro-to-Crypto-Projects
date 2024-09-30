import base64

def decode(text:str):
    ans = ""
    for i in range(0,len(text),2):
        ans = ans + chr(int(text[i:i+2],16))
        ...
    return ans
def encode(text:str):
    print(base64.encode(text))

# print(decode("48657861646563696D616C206973206A757374206F6E65206F66207365766572616C2028696E66696E6974656C792920706F737369626C65207261646963657321"))

cipher = 'QmFzZTY0IGhhcyBhIGxvdCBvZiBjb3VzaW5zIHN1Y2ggYXMgQmFzZTMyLCBCYXNlNTgsIGV0Yy4='
cipher_bytes = base64.b64decode(cipher)
print(cipher_bytes)