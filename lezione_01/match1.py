n:int=(input("inserire un numero di neonati: "))

match n:
    case 1:
        print("congratulazioni")
    case 2:
        print("wow, due gemelli")
    case 3:
        print("wow, tre gemelli")
    case 4:
        print("mamma mia, 4! wow")
    case 5:
        print("incredibile cinque!")
    case _:
        print(f"wow, {n} neonati")