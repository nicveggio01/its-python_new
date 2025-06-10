animali:str=str(input("Inserisci il nome di un animale: "))

mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone", "leone"]
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
        print(f"il programma non è in grado di classificare l'animale inserito ({animali}).")