
def moltiplica(numeri:list[int| float], soglia:int)-> float:

    prodotto=1

    for n in numeri:

        if n < soglia:

            prodotto*= n

        else:
            pass

    return prodotto

casi_di_test = [
    ([1, 2, 3, 4, 5], 4, 6),          
    ([10, 20, 30], 25, 200),          
    ([5, 3, 7, 1], 5, 3),              
    ([5, 6, 7], 5, 1),                 
    ([2, 3, 0, 4], 4, 0),             
    ([], 10, 1),                       
]

for lista, soglia, atteso in casi_di_test:
    risultato = moltiplica(lista, soglia)
    print(f"Lista= {lista}, Soglia= {soglia} ➜ Risultato= {risultato}, Atteso= {atteso}")




            
