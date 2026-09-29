from basics import egcd,to_letters,to_numbers,modinv

def valid_keys():
    valid = []
    for a in range(26):
        if egcd(a,26)[2] == 1:
            valid += [(a,b) for b in range(26)]
    valid.pop(0)
    return valid


def encrypt(plaintext, a, b):
    if egcd(a,26)[2] != 1:
        raise ValueError("offending value")
    return to_letters([(number*a + b) % 26 for number in to_numbers(plaintext)])

def decrypt(ciphertext, a, b):
    return to_letters([modinv(a,26)*(number - b) % 26 for number in to_numbers(ciphertext)])