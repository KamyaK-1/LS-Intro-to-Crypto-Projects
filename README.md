# Intro-to-Crypto-Projects
Contains the files for the projects and file **"Basics.pdf"** which contains the theory I studied for this self project.

## Hill Cipher

The Hill cipher is a classical symmetric encryption algorithm that uses linear algebra to encrypt and decrypt messages. It is one of the earliest examples of polygraphic substitution ciphers. The Hill cipher operates by taking a block of plaintext letters and converting them into a block of ciphertext letters using matrix multiplication.

### How the Hill Cipher Works

1. **Key Matrix**: A key matrix of size $n \times n$ is chosen. This matrix must be invertible (i.e., it must have a non-zero determinant modulo 26 if working with the English alphabet).
2. **Plaintext Vector**: The plaintext is divided into blocks of size $n$. Each block is represented as a vector.
3. **Encryption**: Each plaintext vector is multiplied by the key matrix to produce the ciphertext vector. The operations are performed modulo 26.
4. **Decryption**: The inverse of the key matrix is used to convert the ciphertext vectors back to plaintext vectors.

### Problem Statement

The script consists of two main modes:

**Mode 1: Encryption**
 
 The script should accept a plaintext input, convert it into ciphertext using a given key of size $3 \times 3$, and output the ciphertext. Add padding of 'X' characters to ensure plaintext is a multiple of the key size.

**Mode 2: Key Discovery**

The script should take a known plaintext and its corresponding ciphertext as input and output the key. 

**Note:**
The key size is fixed to be a $3 \times 3$ matrix here.
Ensure the scripts are well-documented and include comments explaining the steps and logic used.

### Testing

Your encryption script should be able to encrypt a message of any size with a given key, where the message and key consist entirely of capital english alphabet letters.

Your decryption script should be able to generate the key matrix given a (plaintext,ciphertext) pair with size more than 9 characters and the matrices formed by resizing the plaintext and ciphertext into a $3 \times 3$ matrix is invertible modulo 26.

The submission will be tested on various input sizes and it is gauranteed that the (plaintext,ciphertext) pairs will form an invertible matrix modulo 26.

### Example
Given the message "ANTCATDOG" and ciphertext "TIMFINWLY", the key produced should be "GYBNQKURP"






## RSA Parity Attack
You have to implement an "adaptive chosen ciphertext" attack on RSA given oracle access to a function that tells you if the decryption of the inputted ciphertext is even or odd.


To achieve that you have to implement the following:
* Create a 1024-bit RSA pair (p,q,e,d,n)
* Implement an encryption function that encrypts a message 'm' with [e,n] to give ciphertext 'c'
* Implement a decryption function that returns the decryption of ciphertext 'c' with [d,n] to give 'm'
* Implement an oracle function that takes as input a ciphertext 'c' and has access to the previously generated secret key 'd' and outputs **True** if Dec(c,d) is odd and **False** if Dec(c,d) is even
* Finally implement a function that takes as input an honest ciphertext 'c' and adaptively queries the oracle with multiple ciphertexts to figure out the decrypted message 'm'




