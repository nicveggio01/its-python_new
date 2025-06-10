
def filtro(carrello:dict[str, float])->dict:

    nuovo_carrello={}

    for prodotto, prezzo in carrello.items():

        if prezzo < 50:

            nuovo_prezzo= round((prezzo* 10)/100), 2
            nuovo_carrello[prodotto]= nuovo_prezzo

        else:
            pass
    
    return nuovo_carrello


