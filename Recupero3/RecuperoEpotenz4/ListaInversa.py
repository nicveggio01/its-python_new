 
#Esercizio base sulle Ricorsioni
def printListBackward(lista:list[int|float|str]):

    if not lista:
        print("")
    else:
        print(lista[-1])
        printListBackward(lista[:-1])

lista=[1,48,98,12]
print(printListBackward(lista))







