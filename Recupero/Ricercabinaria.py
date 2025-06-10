
def ricerca_binaria(numeri:list[int], numero:int)->bool:


    
    numeri.sort()
    inizio=0
    fine=len(numeri)-1
    

    while inizio <= fine:

        centro=(inizio + fine)//2

        if numeri[centro]== numero:
            return True
        elif numeri[centro] < numero:
            inizio=centro + 1
            print("cerca nella metà destra")
        else:
            fine= centro - 1
            print("Cerca nella metà sinistra")
    return False

print(ricerca_binaria([12,45, 87, 2, 65, 4, 91], 12))             
        


    