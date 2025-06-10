nome= input("inserisci il tuo nome: ")
genere= input("inserisci il tuo genere (m per maschio, f per femmina): ")
match genere:
    case "m":
        print(f"nome: {nome}, sesso: maschio")
    case "f":(f"nome: {nome}, sesso: femmina")
    case _: print("genere non riconosciuto")