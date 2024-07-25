import numpy as np  


def encrypt(key:str,plaintext:str):
    key_len = int(len(key)**0.5)
    '''
    key -> 3*3
    text_matrix -> 3*n
    '''
    if (len(key)!=key_len**2):
        return "Invalid Key"
    key = np.array([ord(i)-ord('A') for i in key]).reshape(key_len,key_len) # Matrix reprsented by key
    
    if len(plaintext)%key_len!=0:
        # Adding additional X's to  make the length of plaintext a multiple of key_len
        plaintext = plaintext + 'X'*(key_len-len(plaintext)%key_len)
    
    assert(len(plaintext)%key_len==0)

    text_matrix = np.array([ord(i)-ord('A') for i in plaintext]).reshape(-1,key_len).T # Creating the matrix of input text
    
    result_matrix = ((np.matmul(key,text_matrix))%26).T.reshape(-1)

    return ''.join([chr(i+ord('A')) for i in result_matrix])

def get_key(intext:str,outtext:str):

    if len(intext)%3!=0:
        intext = intext+ 'X'*(3 - len(intext) % 3)# Ensuring the length of input text is multiple of 3

    in_matrix = np.array([ord(i)-ord('A') for i in intext]).reshape(-1,3).T # Matrix representation of input text
    out_matrix = np.array([ord(i)-ord('A') for i in outtext]).reshape(-1,3).T # Matrix representation of output text
 

    assert(in_matrix.shape == out_matrix.shape)
    assert(in_matrix.shape[0]==3)
    
    '''
    Key Matrix * in_matrix = out_matrix
    and all the entries lie between 0 and 25 (inclusive)
    '''
    answer = ""
    found = False
    
    for i in range(26):
        for j in range(26):
            for k in range(26):
                lst = np.array([i,j,k]).reshape(1,3)
                assert(np.matmul(lst,in_matrix).shape[0] == 1)
                # print(np.matmul(lst,in_matrix).shape)
                if np.array_equal((np.matmul(lst,in_matrix))%26,out_matrix[0].reshape(1,-1)): # Checks if the first row of key matrix is correct or not
                    answer += chr(i+ord('A'))+chr(j+ord('A'))+chr(k+ord('A'))
                    
                    found = True
                if found:
                    break
            if found:
                break
        if found:
            break
    if not found:
        print("Failed first")
    found = False    
    for i in range(26):
            for j in range(26):
                for k in range(26):
                    lst = np.array([i,j,k]).reshape(1,3)
                   
                    if np.array_equal((np.matmul(lst,in_matrix))%26,out_matrix[1].reshape(1,-1)): # Checks if the second row of key matrix is correct or not
                        answer += chr(i+ord('A'))+chr(j+ord('A'))+chr(k+ord('A'))
                        found = True
                    if found:
                        break
                if found:
                    break
            if found:
                break
    if not found:
        print("Failed second")
    found = False    
    for i in range(26):
            for j in range(26):
                for k in range(26):
                    lst = np.array([i,j,k]).reshape(1,3)                   
                    if np.array_equal((np.matmul(lst,in_matrix))%26,out_matrix[2].reshape(1,-1)): # Checks if the third row of key matrix is correct or not
                        answer += chr(i+ord('A'))+chr(j+ord('A'))+chr(k+ord('A'))
                        found = True
                    if found:
                        break
                if found:
                    break
            if found:
                break
    if not found:
        print("Failed third")
    return answer
    

    

