from affine import valid_keys, decrypt, encrypt

def chi_squared(text, table):
    l = len(text)
    return sum([(text.count(character) - table[character]*l)**2/(table[character]*l) for character in list(table.keys())])

def break_affine(ciphertext, language="en"):
    if language == "en":
            table = {"A":0.082, "B":0.015, "C":0.028, "D":0.043, "E":0.127, "F":0.022, "G":0.02, "H":0.061, "I":0.07, "J":0.0016, "K":0.077, "L":0.04, "M":0.024, "N":0.067, "O":0.075, "P":0.019, "Q":0.0012, "R":0.06, "S":0.063, "T":0.091, "U":0.028, "V":0.0098, "W":0.024, "X":0.0015, "Y":0.02, "Z":0.074}
    elif language == "es":
            table = {"A":0.1253, "B":0.0142, "C":0.0468, "D":0.0586, "E":0.1368, "F":0.0069, "G":0.0101, "H":0.007, "I":0.0625, "J":0.0044, "K":0.0002, "L":0.0497, "M":0.0315, "N":0.0671, "Ñ":0.0031, "O":0.0868, "P":0.0251, "Q":0.0088, "R":0.0687, "S":0.0798, "T":0.0463, "U":0.0393, "V":0.009, "W":0.0001, "X":0.0022, "Y":0.009, "Z":0.0052}
   

    val_keys = valid_keys()


    resultado = ((val_keys[0][0],val_keys[0][1]), chi_squared(decrypt(ciphertext,*val_keys[0]),table))
    
    for key in val_keys:
        if chi_squared(decrypt(ciphertext,*key), table) < resultado[1]:
            resultado = ((key[0], key[1]), chi_squared(decrypt(ciphertext,*key), table))


    return (resultado[0], decrypt(ciphertext,*resultado[0]))
    




