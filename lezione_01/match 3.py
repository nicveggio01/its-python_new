voto= int(input("digitare il voto: "))
match voto:
    case 10:
        print("voto ottimo")
    case 8 | 9:
        print("voto molto buono")
    case 6 | 7:
        print("voto sufficiente")
    case 4 | 5:
        print("voto insufficiente")
    case 1 | 2 | 3:
        print("gravemente insufficiente")
    case _:
        print("voto non valido")