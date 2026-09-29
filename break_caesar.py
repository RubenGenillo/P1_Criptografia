from caesar import decrypt, encrypt

def chi_squared(text, table):
    l = len(text)
    return sum([(text.count(character) - table[character]*l)**2/(table[character]*l) for character in list(table.keys())])


def break_caesar(ciphertext, language="en"):
    if language == "en":
        table = {"A":0.082, "B":0.015, "C":0.028, "D":0.043, "E":0.127, "F":0.022, "G":0.02, "H":0.061, "I":0.07, "J":0.0016, "K":0.077, "L":0.04, "M":0.024, "N":0.067, "O":0.075, "P":0.019, "Q":0.0012, "R":0.06, "S":0.063, "T":0.091, "U":0.028, "V":0.0098, "W":0.024, "X":0.0015, "Y":0.02, "Z":0.074}
    elif language == "es":
        table = {"A":0.1253, "B":0.0142, "C":0.0468, "D":0.0586, "E":0.1368, "F":0.0069, "G":0.0101, "H":0.007, "I":0.0625, "J":0.0044, "K":0.0002, "L":0.0497, "M":0.0315, "N":0.0671, "Ñ":0.0031, "O":0.0868, "P":0.0251, "Q":0.0088, "R":0.0687, "S":0.0798, "T":0.0463, "U":0.0393, "V":0.009, "W":0.0001, "X":0.0022, "Y":0.009, "Z":0.0052}
    resultado = (0, chi_squared(decrypt(ciphertext,0),table))
    for k in range(1,26):
        if chi_squared(decrypt(ciphertext,k),table) < resultado[1]:
            resultado = (k, chi_squared(decrypt(ciphertext,k),table))

    return (resultado[0], decrypt(ciphertext,resultado[0]))

if __name__ == "__main__":
    from nltk.corpus import brown
    from nltk.corpus import cess_esp
    import random


    words = brown.words()
    words = "".join([word for word in words if word.isalpha()])
    words = words.upper()

    palabras = cess_esp.words()
    palabras = "".join([palabra for palabra in palabras if palabra.isalpha()])
    palabras = palabras.upper()
    palabras = palabras.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")

    random.seed(2)    

    sample_20 = []
    sample_30 = []
    sample_40 = []
    sample_60 = []
    sample_100 = []

    muestra_20 = []
    muestra_30 = []
    muestra_40 = []
    muestra_60 = []
    muestra_100 = []

    for i in range(200):

        index = random.randint(0,len(words)-20)
        sample_20.append(words[index:index + 20])
        index = random.randint(0,len(words)-30)
        sample_30.append(words[index:index + 30])
        index = random.randint(0,len(words)-40)
        sample_40.append(words[index:index + 40])
        index = random.randint(0,len(words)-60)
        sample_60.append(words[index:index + 60])
        index = random.randint(0,len(words)-100)
        sample_100.append(words[index:index + 100])

        indice = random.randint(0,len(palabras)-20)
        muestra_20.append(palabras[indice:indice + 20])
        indice = random.randint(0,len(palabras)-30)
        muestra_30.append(palabras[indice:indice + 30])
        indice = random.randint(0,len(palabras)-40)
        muestra_40.append(palabras[indice:indice + 40])
        indice = random.randint(0,len(palabras)-60)
        muestra_60.append(palabras[indice:indice + 60])
        indice = random.randint(0,len(palabras)-100)
        muestra_100.append(palabras[indice:indice+100])



    key_obtained_20 = []
    key_obtained_30 = []
    key_obtained_40 = []
    key_obtained_60 = []
    key_obtained_100 = []

    clave_obtenida_20 = []
    clave_obtenida_30 = []
    clave_obtenida_40 = []
    clave_obtenida_60 = []
    clave_obtenida_100 = []

    clave_obtained_20 = []
    clave_obtained_30 = []
    clave_obtained_40 = []
    clave_obtained_60 = []
    clave_obtained_100 = []

    for sample in sample_20:
        k = random.randint(0,26)
        key_obtained_20.append(break_caesar(encrypt(sample, k))[0] == k)
    for sample in sample_30:
        k = random.randint(0,26)
        key_obtained_30.append(break_caesar(encrypt(sample, k))[0] == k)
    for sample in sample_40:
        k = random.randint(0,26)
        key_obtained_40.append(break_caesar(encrypt(sample, k))[0] == k)
    for sample in sample_60:
        k = random.randint(0,26)
        key_obtained_60.append(break_caesar(encrypt(sample, k))[0] == k)
    for sample in sample_100:
        k = random.randint(0,26)
        key_obtained_100.append(break_caesar(encrypt(sample, k))[0] == k)

    for muestra in muestra_20:
        k = random.randint(0,26)
        clave_obtained_20.append(break_caesar(encrypt(muestra,k))[0] == k)
    for muestra in muestra_30:
        k = random.randint(0,26)
        clave_obtained_30.append(break_caesar(encrypt(muestra,k))[0] == k)
    for muestra in muestra_40:
        k = random.randint(0,26)
        clave_obtained_40.append(break_caesar(encrypt(muestra,k))[0] == k)
    for muestra in muestra_60:
        k = random.randint(0,26)
        clave_obtained_60.append(break_caesar(encrypt(muestra,k))[0] == k)
    for muestra in muestra_100:
        k = random.randint(0,26)
        clave_obtained_100.append(break_caesar(encrypt(muestra,k))[0] == k)


    for muestra in muestra_20:
        k = random.randint(0,26)
        clave_obtenida_20.append(break_caesar(encrypt(muestra,k), "es")[0] == k)
    for muestra in muestra_30:
        k = random.randint(0,26)
        clave_obtenida_30.append(break_caesar(encrypt(muestra,k), "es")[0] == k)
    for muestra in muestra_40:
        k = random.randint(0,26)
        clave_obtenida_40.append(break_caesar(encrypt(muestra,k), "es")[0] == k)
    for muestra in muestra_60:
        k = random.randint(0,26)
        clave_obtenida_60.append(break_caesar(encrypt(muestra,k), "es")[0] == k)
    for muestra in muestra_100:
        k = random.randint(0,26)
        clave_obtenida_100.append(break_caesar(encrypt(muestra,k), "es")[0] == k)


    print("en_20", sum(key_obtained_20)/200)
    print("en_30", sum(key_obtained_30)/200)
    print("en_40", sum(key_obtained_40)/200)
    print("en_60", sum(key_obtained_60)/200)
    print("en_100", sum(key_obtained_100)/200)

    print("es_20", sum(clave_obtenida_20)/200)
    print("es_30", sum(clave_obtenida_30)/200)
    print("es_40", sum(clave_obtenida_40)/200)
    print("es_60", sum(clave_obtenida_60)/200)
    print("es_100", sum(clave_obtenida_100)/200)

    print("es_en_20", sum(clave_obtained_20)/200)
    print("es_en_30", sum(clave_obtained_30)/200)
    print("es_en_40", sum(clave_obtained_40)/200)
    print("es_en_60", sum(clave_obtained_60)/200)
    print("es_en_100", sum(clave_obtained_100)/200)