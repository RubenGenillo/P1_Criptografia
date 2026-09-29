from basics import to_letters, to_numbers

def encrypt(plaintext,k):
    k = k % 26
    return to_letters([(number + k)%26 for number in to_numbers(plaintext)])

def decrypt(ciphertext, k):
    k = k % 26
    return to_letters([(number - k)%26 for number in to_numbers(ciphertext)])