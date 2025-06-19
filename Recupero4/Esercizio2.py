

def proDict()-> dict[tuple, int]:

    mydict:dict[tuple, int]={}

    for x in range(0,101):
        for y in range(2,89, 2):
            prodotto=x*y
            mydict[x,y]= prodotto
            
    return mydict

print(proDict())

        

