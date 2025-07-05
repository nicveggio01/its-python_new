
import random

def genera(dim:int):

    matrice=[]

    for i in range(dim):
        riga=[]

        primo_numero= random.randint(0,13)
        riga.append(primo_numero)

        for j in range(dim -1):

            numero= random.randint(0,13)

            while numero == primo_numero:
                numero= random.randint(0,13)
            riga.append(numero)
        matrice.append(riga)
    return matrice


def printMat(matrice:list[list[int]]):

    if len(matrice) > 5:
        raise ValueError("La matrice ha più di 5 righe.")
    return matrice

def calcolacarico(matrice:list[list[int]], r:int, c:int)->int:

    if r < 0 or c < 0:
        raise ValueError("Errore non può essereci una riga con indiice negativa tantomeno le colonne.")
    if r >= len(matrice) or c >= len(matrice[0]):
        raise ValueError("Gli indici superano le dimensioni della matrice")
    
    somma_riga= sum(matrice[r])
    somma_colonna=sum(matrice[i][c] for i in range(len(matrice)))

    carico= somma_riga - somma_colonna

    return carico

def caricoNullo(matrice:list[list[int]], r:int, c:int)->list[tuple[int, int]]:
    if not matrice or not matrice[0]:
        raise ValueError("La matrice non può essere vuota")
    
    numero_righe= len(matrice)
    numero_colonne= len(matrice[0])

    somma_righe= [sum(riga) for riga in matrice]
    somme_colonne = [sum(matrice[i][c] for i in range(numero_righe)) for c in range(numero_colonne)]

    carico_nullo=[]

    for r in range(numero_righe):
        for c in range(numero_colonne):
            carico= somma_righe[r] - somme_colonne[c]
            if carico==0:
                carico_nullo.append((r,c))
    
    return carico_nullo

def caricoMin(matrice: list[list[int]]) -> tuple[int, int]:

    if not matrice or not matrice[0]:
        raise ValueError("La matrice non può essere vuota")
    
    numero_righe= len(matrice)
    numero_colonne= len(matrice[0])

    somma_righe= [sum(riga) for riga in matrice]
    somme_colonne = [sum(matrice[i][c] for i in range(numero_righe)) for c in range(numero_colonne)]

    carico_min=0

    for r in range(numero_righe):
        for c in range(numero_colonne):
            carico= somma_righe[r] - somme_colonne[c]
            if carico < carico_min:
                carico_min= carico
    
    return carico_min






   


    




        




