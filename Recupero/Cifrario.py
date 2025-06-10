
from string import ascii_lowercase

def caesar_cypher_encrypt(s, key):

    risultato=""

    if key < 0:
        print("Errore la chiave non può essere negativa")
    else:
        for char in s:
            if char in ascii_lowercase:
               posizione= ascii_lowercase.index(char)
               nuova_posizione= posizione + key % 26
               risultato += ascii_lowercase[nuova_posizione]
            else:
                risultato += char
        return risultato

print(caesar_cypher_encrypt("ciao", 2))

def caesar_cypher_decrypt(s, key):
    risultato=""

    if key < 0:
        print("Errore la chiave non può essere negativa")
    else:
        for char in s:
            if char in ascii_lowercase:
               posizione= ascii_lowercase.index(char)
               nuova_posizione= (posizione) - key % 26
               risultato += ascii_lowercase[nuova_posizione]
            else:
                risultato += char
        return risultato

print(caesar_cypher_decrypt("ekcq", 2))

