from vigenere import cosets, decrypt
from break_caesar import break_caesar
from basics import to_letters

def break_vigenere(ciphertext, m, language = "en"):
    """m is the key length, given to you. Returns (key, plaintext)."""
    key = []
    for text in cosets(ciphertext,m):
        key.append(break_caesar(text, language)[0])
        
    return (to_letters(key), decrypt(ciphertext,to_letters(key)))

if __name__ == "__main__":
    from vigenere import encrypt
    from nltk.corpus import brown
    from nltk.corpus import cess_esp
    import random
    
    def testing(m, l, t, language):
            if language == "en":
                words = brown.words()
                words = "".join([word for word in words if word.isalpha()])
                words = words.upper()
            elif language == "es":
                words = cess_esp.words()
                words = "".join([palabra for palabra in words if palabra.isalpha()])
                words = words.upper()
                words = words.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
            
            random.seed(2)    
        
            test_sample = []

            for i in range(t):
                index = random.randint(0,len(words)-l)
                test_sample.append(words[index:index + l])
                
            key_obtained = []

            for sample in test_sample:
                k =  to_letters([random.randint(0,25) for i in range(m)])
                key_obtained.append(break_vigenere(encrypt(sample, k), m)[0] == k)
        
            print(language+"_"+str(l)+"_"+str(m), sum(key_obtained)/t)


    for language in ["en","es"]:
         for k in [3,5,7]:
            for l in [60,120,200,300]:
                testing(k,l,200,language)