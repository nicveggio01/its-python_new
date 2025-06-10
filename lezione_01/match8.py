animali:str=str(input("Inserisci il nome di un animale: "))
categoria:str=str(input("Inserisci la categoria dell'animale (mammiferi, rettili, uccelli, pesci): "))
mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone", "leone", "balena", "delfino"]
rettili: list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list=["aquila", "pappagallo", "gufo", "falco"]
pesci:list=["squalo", "trota", "salmone", "carpa"]

match animali.lower():

    case animal if animal in mammiferi:
        print(f"{animal} è un mammifero")
    case animal if animal in rettili:
        print(f"{animal} è un rettile")
    case animal if animal in uccelli:
        print(f"{animal} è un uccello")
    case animal if animal in pesci:
        print(f"{animal} è un pesce")
    case _:
        print("Unknown")

habitat:list=["terra", "acqua", "aria"]
    
def verifica_habitat(animal: str) -> str:
    match animal:
        case animal if animal in mammiferi:
            print(f"{animal} vive sulla terra")
        case animal if animal in rettili:
            print(f"{animal} vive sulla terra")
        case animal if animal in uccelli:
            print(f"{animal} vive in aria")
        case animal if animal in pesci:
            print(f"{animal} vive in acqua")
        case _:
            print("Unknown")
match categoria, habitat:
        case "mammiferi", "terra":
            print(f"{"cane", "gatto", "cavallo", "elefante", "leone"} vive sulla terra")
        case "mammiferi", "acqua":
            print(f"{"balena", "delfino"} vive in acqua")
        case "rettili", "terra":
            print(f"{"serpente", "lucertola", "tartaruga"} vive sulla terra")
        case "rettili", "acqua":
            print(f"{"coccodrillo"} vive in acqua")
        case "uccelli", "terra":
            print(f"{"gallina", "tacchino"} vive sulla terra")
        case "uccelli", "acqua":
            print(f"{"cigno","anatra"} vive in acqua")
        case "uccelli", "aria":
            print(f"{"aquila", "pappagallo", "gufo", "falco"} vive in aria")
        case "pesci", "acqua":
            print(f"{"squalo", "trota", "salmone", "carpa"} vive in acqua")

#classificare gli animali in base alla categoria e all'habitat

animale_info:dict={
    "nome":animal,
    "categoria":categoria,
    "habitat":habitat
}

print(animale_info)