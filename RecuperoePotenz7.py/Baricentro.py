
def baricentro(v:list[int])->int:
    if not v:
        raise ValueError("Errore impossibile calcolare il baricentro, lista vuota")
    
    somma_totale=sum(v)
    somma_sinistra=0
    

    for i in range(len(v)):
        somma_destra= somma_totale - somma_sinistra - v[i]
        if somma_sinistra == somma_destra:
            return i
        somma_sinistra += v[i]
    

v=[1, 2, 3, 2 ,1]
print(baricentro(v))







    