
def ordina(lista:list[int|float] )-> dict[str: list| int| float]:

    my_dict={}

    lista_positivi=[]
    lista_negativi=[]

    for l in lista:

        if l < 0:
            lista_negativi.append(l)
        else:
            lista_positivi.append(l)
        
        my_dict["lista_negativi"]= lista_negativi
        my_dict["lista positivi"]= lista_positivi
    
    return my_dict

        
