
def is_integer(valore):
    return isinstance(valore, int)
def intero_positivo(testo="Inserisci un numero intero positivo:"):
    while True:
        try:    
            x= int(input(testo))
            if x < 0:
                print("Errore inserire un numero positivo.")
            else:
                return x
        except ValueError:
            print("Errore inserire un numero valido.")



x= intero_positivo("Inserisci il numero intero positivo x: ")
print(f"Hai inserito il numero {x}")

# Sequenza

sequenza=[]

while True:
    numero= intero_positivo("Inserisci un numero intero positivo (0 per terminare):")
    if numero== 0:
        break
    else:
        sequenza.append(numero)

print(f"Sequenza:{sequenza}")

occorrenze=0
somma_valori_diversi_da_x=0

if x in sequenza:
    indice= sequenza.index(x)
    print(f"Il numero {x} appare nella sequenza all'indice {indice}")
else:
    print(f"{x} non appartiene alla sequenza")

for numero in sequenza:
    if numero==x:
        occorrenze+=1
    else:
        somma_valori_diversi_da_x += numero
print(f"Il numero {x} appare {occorrenze} volte")
print(f"La somma di tutti i valori nella sequenza diversi da {x} è {somma_valori_diversi_da_x}")










