
def verifica_condizioni(x:bool, y:bool, z:bool)-> str:

    if x==True and (y==True or x==True):
        return("Azione permessa")
    else:
        return("Azione negata")



combinazioni = [
    (True, True, False),   
    (True, False, True),   
    (True, False, False),  
    (False, True, True),   
    (False, False, False), 
]

for x, y, z in combinazioni:
    risultato = verifica_condizioni(x, y, z)
    print(f"X={x}, Y={y}, Z={z} ➜ {risultato}")


