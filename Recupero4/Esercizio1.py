basi={
"A": "adenina",
"C":"citosina",
"G":"guanina",
"T":"timina",
}


s1= str(input("Inserisci una sequenza di basi azotate(A:adenina, C:citosina, G:guanina, T:timina) che andranno a formare il singolo filamento s1: ").upper())

if any(c not in basi for c in s1 ):
    raise ValueError("Errore filamento di basi azotate non valido.")

s2=str(input("Inserisci una sequenza di basi azotate(A:adenina, C:citosina, G:guanina, T:timina) che andranno a formare il singolo filamento s1: ").upper())
if any(c not in basi for c in s2):
    raise ValueError("Errore filamento di basi azotate non valido.")

lunghezza=int(input("Inserisci la massima lunghezza di sovrapposizione: "))

s1_last= s1[-lunghezza:]
s2_first= s2[:lunghezza]
sovrapposte=""

for i, j in zip(s1_last, s2_first):
    if i==j:
        sovrapposte += i

if sovrapposte:
    print(f"I due filamenti {s1} e {s2} di basi azotate hanno {len(sovrapposte)} basi sovrapponibili. ")
else:
    print(f"I due filamenti {s1} e {s2} non sono sovrapponibili. Nessuna base corrisponde.")





