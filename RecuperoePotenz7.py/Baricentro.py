
def baricentro(v:list[int])->int|None: 
    if not v:
        raise ValueError("Errore impossibile calcolare il baricentro, lista vuota")
    
    somma_totale=sum(v)
    somma_sinistra=0
    

    for i in range(len(v)):
        somma_destra= somma_totale - somma_sinistra - v[i]
        if somma_sinistra == somma_destra:
            return i
        somma_sinistra += v[i]
    return None    

def printresult(v:list[int]):
    b= baricentro(v)
    if not b:
        print(f"Il baricentro del vettore {v} non esiste.")
    else:
        print(f"Esiste il baricentro del vettore {v} ed è dato dall'indice {b}")
    

v=[1, 2, 3, 2 ,1]
print(baricentro(v))
printresult(v)
v2 = [2, 0, -1, 4, 6, 3, -1]
print(baricentro(v2))
printresult(v2)









    