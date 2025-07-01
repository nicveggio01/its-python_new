
# Esercizio Tariffe Parcheggio
import math


ore_parcheggiate=int(input("Inserisci il numero di ore di parcheggio: "))



def calculateCharges(ore_parcheggiate:int)->float:
    costo=0

    if ore_parcheggiate <=3:
        costo=2
        return costo
    elif ore_parcheggiate > 3 and ore_parcheggiate <= 24:
        ore_parcheggiate= math.ceil(ore_parcheggiate)
        costo = ((ore_parcheggiate-3)*0.5) + 2
        return costo
    else:
        costo=10
        return costo

print(calculateCharges(ore_parcheggiate))

    
clienti=[1.5, 4.0, 5.5, 24]
print(f"{'Car':<10} {'hours':<10} {'charges':<10}")
total=0

for item in clienti:
    c= calculateCharges(item)
    total += c
    print(f"{clienti.index(item)+1:<10} {item:<10} {c:<10.2f}")

print(f"{'total':<10} {sum(clienti):<10} {total:<2f}")


print(calculateCharges(6))

