
'''La funzione prende una lista di stringhe words e un intero min_length.
Deve restituire una stringa contenente tutte le parole di words che hanno lunghezza maggiore di min_length, 
concatenate tra loro separate da uno spazio.'''




def extract_and_join(words: list[str], min_length: int) -> str:

    frase=""

    for w in words:
        if len(w) > min_length:
            frase += w + " "
        else:
            pass

    return frase

print(extract_and_join(["ciao", "a", "Niccolo", "bellissimo", "lio"], 3))


