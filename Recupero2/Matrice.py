
def sum_primary_diagonal(matrice:list[list[int]])-> int:

    somma_diagonale1=0

    for i in range(len(matrice)):
        # essendo una matrice quadrata l'indice della riga in questo caso è sempre uguale a quello della colonna 0x0, 1x1, 2x2; per quanto riguarda la somma diagonale primaria da sx adx
        somma_diagonale1+=matrice[i][i]

    return somma_diagonale1

def sum_secondary_diagonal(matrice:list[list[int]])-> int:

    somma_diagonale2=0

    for i in range(len(matrice)):
        # per quanto riguarda la somma della diagonale secondaria, faccio 0x2, 1x1, 2x0; 
        somma_diagonale2+=matrice[i][len(matrice)-1- i]
    return somma_diagonale2


mat1 = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9] 
] 
print(sum_primary_diagonal(mat1))
print(sum_secondary_diagonal(mat1))


          
