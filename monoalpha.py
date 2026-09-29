def key_from_keyboard(keyword):
    characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return keyword + "".join([character for character in characters if character not in keyword])        

def permited_key(key):
    characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return len(key) == 26 and min ([character in key for character in characters] )

def encrypt(plaintext, key):
    if not permited_key(key):
        raise ValueError("Not permited key")
    characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ciphertext = ""
    for character in plaintext:
        ciphertext += key[characters.index(character)]
    return ciphertext

def decrypt(ciphertext, key):
    if not permited_key(key):
        raise ValueError("Not permited key")
    characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    plaintext = "" 
    for character in ciphertext:
        plaintext += characters[key.index(character)]
    return plaintext      