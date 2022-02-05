from Crypto.Cipher import AES
# we use os to produce random character according to size (byte) 
import os 

# 128 bits or 16 bytes
size = 16
padding_char = ')'
BLOCK_SIZE = 16
key = os.urandom(size)



# encrypt a plaintext 
def encrypt(plaintext):
    aes = AES.new(key=key,mode=AES.MODE_ECB)
    plaintext = padding(plaintext)
    return aes.encrypt(plaintext.encode('utf-8'))

# here we are sure that plaintext multiplication of block size
def padding(text: str):
    text += ((BLOCK_SIZE - len(text)) % BLOCK_SIZE) * padding_char
    return text

# decrypt an encrypted plaintext 
def decrypt(encrypted_plaintext):
    aes = AES.new(key=key,mode=AES.MODE_ECB)
    plaintext = aes.decrypt(encrypted_plaintext).decode('utf-8')
    plaintext = reverse_padding(plaintext)
    return plaintext


# here we remove padding character that we add to plaintext multiplication of block size
def reverse_padding(text: str):
    padding_char_index = text.find(padding_char)
    # extract text witout padding character
    text = text[:padding_char_index]
    return text
