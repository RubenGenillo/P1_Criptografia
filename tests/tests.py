from nltk.corpus import brown
from nltk.corpus import cess_esp
import random
from affine import encrypt, decrypt, valid_keys
from break_affine import break_affine


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

valid_k = valid_keys()
for sample in sample_20:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    key_obtained_20.append(break_affine(encrypt(sample, *k))[0] == k)
for sample in sample_30:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    key_obtained_30.append(break_affine(encrypt(sample, *k))[0] == k)
for sample in sample_40:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    key_obtained_40.append(break_affine(encrypt(sample, *k))[0] == k)
for sample in sample_60:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    key_obtained_60.append(break_affine(encrypt(sample, *k))[0] == k)
for sample in sample_100:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    key_obtained_100.append(break_affine(encrypt(sample, *k))[0] == k)

for muestra in muestra_20:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtained_20.append(break_affine(encrypt(muestra,*k))[0] == k)
for muestra in muestra_30:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtained_30.append(break_affine(encrypt(muestra,*k))[0] == k)
for muestra in muestra_40:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtained_40.append(break_affine(encrypt(muestra,*k))[0] == k)
for muestra in muestra_60:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtained_60.append(break_affine(encrypt(muestra,*k))[0] == k)
for muestra in muestra_100:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtained_100.append(break_affine(encrypt(muestra,*k))[0] == k)


for muestra in muestra_20:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtenida_20.append(break_affine(encrypt(muestra,*k), "es")[0] == k)
for muestra in muestra_30:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtenida_30.append(break_affine(encrypt(muestra,*k), "es")[0] == k)
for muestra in muestra_40:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtenida_40.append(break_affine(encrypt(muestra,*k), "es")[0] == k)
for muestra in muestra_60:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtenida_60.append(break_affine(encrypt(muestra,*k), "es")[0] == k)
for muestra in muestra_100:
    k =valid_k[random.randint(0,len(valid_k) - 1)]
    clave_obtenida_100.append(break_affine(encrypt(muestra,*k), "es")[0] == k)


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