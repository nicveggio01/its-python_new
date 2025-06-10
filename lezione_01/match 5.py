oggetti=[]
oggetti.append("penna")
oggetti.append("quaderno")
oggetti.append("matita")

match oggetti: 
    case ["penna", "quaderno", "matita"]:
        print("materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("mobili")
    case ["telefono", "computer", "tablet"]:
        print("dispositivi elettronici")
    case _:
        print("categoria non riconosciuta")