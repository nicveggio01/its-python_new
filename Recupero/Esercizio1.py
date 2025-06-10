
def converti(lista:list[tuple])-> dict:

    dict={}

    for element in lista:

        key, value= element[0],element[1]

        if key in dict:
            dict[1] += value
        else:
            dict[key]= value
            
    return dict
            


