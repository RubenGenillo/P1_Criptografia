from basics import to_numbers, to_letters
def cosets(ciphertext, m):
    return[ciphertext[i:len(ciphertext):m] for i in range(m)]
    

def encrypt(plaintext, key):
    if not key.isalpha():
        raise ValueError("Not permited key")
    plaintext = to_numbers(plaintext)
    key = to_numbers(key)
    m = len(key)
    ciphertext = []

    for i in range(len(plaintext)):
        ciphertext.append((plaintext[i] + key[i%m]) % 26)
    
    return to_letters(ciphertext)


def decrypt(ciphertext, key):
    if not key.isalpha():
        raise ValueError("Not permited key")
    ciphertext = to_numbers(ciphertext)
    key = to_numbers(key)
    m = len(key)
    plaintext = []    

    for i in range(len(ciphertext)):
            plaintext.append((ciphertext[i] - key[i%m]) % 26)

    return to_letters(plaintext)