# import the necessary libraries here
import Crypto
from Crypto.Random import random
import Crypto.Random
import Crypto.Util
from Crypto.Util.number import bytes_to_long, long_to_bytes
import random

import Crypto.Util.number

def modular_inv(a,b):
    x = 1 
    y = 0
    x1 = 0 
    y1 = 1
    a1 = a
    b1 = b

    while b1!=0:
        q = a1//b1
        (x,x1) = (x1, x - q*x1)
        (y,y1) = (y1, y - q*y1)
        (a1,b1) = (b1, a1 - q*b1)
    return x,y
    
class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length):
       
        self.p = Crypto.Util.number.getPrime(key_length)
        self.q = Crypto.Util.number.getPrime(key_length)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        random_extra_bits = random.randint(1,key_length-1)
        self.e = Crypto.Util.number.getPrime(key_length+random_extra_bits) # If e has more bits than p and q and e is prime then it is coprime with (p-1)(q-1) as (p-1)(q-1) has all its prime factors <max(p,q) and e > max(p,q) 
        
        self.d = (modular_inv( self.phi , self.e)[1]) % self.phi  # In python remainder always returns a number with same sign as the divisor. Since our divisor is positive, taking remainder ensures that d is always positive
        assert(self.d > 0 and (self.d * self.e) % self.phi == 1 and Crypto.Util.number.GCD(self.e,self.phi) == 1)

    def encrypt(self, binary_data):
        # return encryption of binary_data here
        return pow(bytes_to_long(binary_data), self.e, self.n)


    def decrypt(self, encrypted_int_data):
        # return decryption of encrypted_binary_data here
        return long_to_bytes(pow(encrypted_int_data, self.d, self.n)).decode()

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""

    def is_parity_odd(self, encrypted_int_data) -> bool:
        return True if pow(encrypted_int_data, self.d, self.n) % 2 == 1 else False



def parity_oracle_attack(ciphertext, rsa_parity_oracle:RSAParityOracle):
    l = 0 
    r = rsa_parity_oracle.n - 1
    power = pow(2,rsa_parity_oracle.e,rsa_parity_oracle.n)
    original_text = ciphertext
    while l < r:
        mid = (l+r)//2
        ciphertext = (ciphertext*power)%rsa_parity_oracle.n
        if rsa_parity_oracle.is_parity_odd(ciphertext):
            l = mid + 1
        else:
            r = mid 
    # for step in range(l,r+1):
    #     if rsa_parity_oracle.is_parity_odd((ciphertext*pow(2,step,rsa_parity_oracle.n))%rsa_parity_oracle.n):
    #         return long_to_bytes(step).decode()
    #     ...

    # ...
    l = l & (~0xff)
    for i in range(0,256):
        try:
            if (rsa_parity_oracle.encrypt(long_to_bytes(l+i)) == original_text): # Encryption key is visible to all so 
                return long_to_bytes(l+i)
        except UnicodeDecodeError:
            pass


def main():
    
    input_bytes = input("Enter the message: ")
    print(input_bytes.encode())
    # Generate a 1024-bit RSA pair    
    rsa_parity_oracle = RSAParityOracle(1024)

    # Encrypt the message
    ciphertext = rsa_parity_oracle.encrypt(input_bytes.encode())
    print("Encrypted message is: ",ciphertext)
    print("Decrypted text is: ",rsa_parity_oracle.decrypt(ciphertext))
    assert(rsa_parity_oracle.decrypt(ciphertext) == input_bytes)
    # Check if the attack works
    plaintext = parity_oracle_attack(ciphertext, rsa_parity_oracle)
    print("Obtained plaintext: ",plaintext)
    assert plaintext == input_bytes.encode()


if __name__ == '__main__':
    main()