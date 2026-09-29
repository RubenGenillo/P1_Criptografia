def report(ciphertext, language="en"):
    if language == "en":
            table = {"A":0.082, "B":0.015, "C":0.028, "D":0.043, "E":0.127, "F":0.022, "G":0.02, "H":0.061, "I":0.07, "J":0.0016, "K":0.077, "L":0.04, "M":0.024, "N":0.067, "O":0.075, "P":0.019, "Q":0.0012, "R":0.06, "S":0.063, "T":0.091, "U":0.028, "V":0.0098, "W":0.024, "X":0.0015, "Y":0.02, "Z":0.074}
    elif language == "es":
            table = {"A":0.1253, "B":0.0142, "C":0.0468, "D":0.0586, "E":0.1368, "F":0.0069, "G":0.0101, "H":0.007, "I":0.0625, "J":0.0044, "K":0.0002, "L":0.0497, "M":0.0315, "N":0.0671, "Ñ":0.0031, "O":0.0868, "P":0.0251, "Q":0.0088, "R":0.0687, "S":0.0798, "T":0.0463, "U":0.0393, "V":0.009, "W":0.0001, "X":0.0022, "Y":0.009, "Z":0.0052}

    characters = list(table.keys())
    values = list(table.values())
    index_table = sorted(range(len(list(table.values()))), key=lambda i: list(table.values())[i])
    table_ordered = [characters[i] for i in index_table]
    table_values_ordered = [values[i] for i in index_table]

    count = [ciphertext.count(character) for character in characters]
    porcentage = [letter/len(ciphertext) for letter in count]
    index = sorted(range(len(count)), key=lambda i: count[i])
    trigrams = [ciphertext[i:i+3] for i in range(len(ciphertext) - 3)]
    trigrams_unique = list(dict.fromkeys(trigrams))
    bigrams = [ciphertext[i:i+2] for i in range(len(ciphertext) - 2)]
    bigrams_unique = list(dict.fromkeys(bigrams))
    bigrams_count = [ciphertext.count(bigram) for bigram in bigrams_unique]
    index_bigram = sorted(range(len(bigrams_count)), key=lambda i: bigrams_count[i])

    print("Distribution | Expected distribution")
    initial_mapping = ciphertext
    j = 0
    for i in index:
        print(characters[i]  +" porcentage: "+ str(porcentage[i])+ " counts: "+ str(count[i])+ " | "+table_ordered[j]+": "+str(table_values_ordered[j]))
        if count[i] != 0:
              initial_mapping= initial_mapping.replace(characters[i],table_ordered[j].lower())
        j+=1
    print("\nTrigrams:") 
    for result in [(trigram, ciphertext.count(trigram), [i for i, value in enumerate(trigrams) if value == trigram]) for trigram in trigrams_unique if ciphertext.count(trigram) > 1]:
          print(result[0]+ " count: "+ str(result[1]) + " positions: "+ str(result[2]))
    print("\nTop 10 most frequent bigrams:") 
    for i in index_bigram[::-1][0:10]:
          print(bigrams_unique[i] )
    print("\nDuplicated letters")
    print(list(dict.fromkeys([ciphertext[i] for i in range(len(ciphertext) - 1) if ciphertext[i] == ciphertext[i+1]])))
    print("\nSuggested initial mapping: ",initial_mapping.upper())         

report("QATNTYSMHQXJOCYHKATMFSNQITUTMPTKTIPJIDTTKHIGQATCEGJMHQAFNTYMTQRTYCSNTJIEXQATDTXYCIRTYACIGTPVATIHQHNYJFKMJFHNTP")

