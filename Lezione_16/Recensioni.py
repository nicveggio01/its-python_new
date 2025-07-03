
class Media:

    _titolo:str
    _reviews:list[int]

    def __init__(self, titolo:str, reviews:list[int]):

        self._titolo= titolo

        for r in reviews:
            if r > 5 or r < 1:
                raise ValueError("La recensione può avere come valori solo tra 1 e 5 compresi.")
        self._reviews=reviews
    
    def set_title(self, titolo:str):
        self._titolo=titolo
    def get_titolo(self)->str:
        return self._titolo
    def aggiungi_valutazione(self, voto: int):

        if voto > 5 or voto < 1:
            raise ValueError("Errore impossibile aggiungere il voto, in quanto non valido.")
        else:
            self._reviews.append(voto)
    
    def GetMedia(self)-> float:

        if not self._reviews:
            return 0
        
        somma=0

        for voto in self._reviews:
            somma += voto
        media= somma/len(self._reviews)
        return media
    
    def GetRate(self)-> str:

        media= self.GetMedia()
        voto= round(media)

        if voto==1:
            return "Terribile"
        elif voto==2:
            return "Brutto"
        elif voto==3:
            return "Normale"
        elif voto==4:
            return "Bello"
        else:
            return "Grandioso"
    
    def ratePercentage(self, voto):

        if voto < 1 or voto > 5:
            raise ValueError("Voto non valido.")

        conteggio=0
        
        for v in self._reviews:
            if v==voto:
                conteggio +=1
        if not self._reviews:
            return 0
        
        percentuale=(conteggio/len(self._reviews))*100
        return percentuale
      

    def recensione(self):

        print(f"Titolo del Film: {self.get_titolo()}")
        print(f"Voto Medio: {self.GetMedia()}")
        print(f"Giudizio: {self.GetRate()}")
        
        giudizi={
            1:"Terribile", 
            2:"Brutto",
            3:"Normale",
            4:"Bello",
            5:"Grandioso"
        }

        for i in range(1, 6):
            print(f"{giudizi[i]}: {self.ratePercentage(i)}%")



film1= Media("Star Wars", [4, 5, 3, 4, 4, 2, 5, 4, 2, 3])
film2= Media("Interstellar", [5, 5, 4, 5, 3, 5, 4, 4, 3, 4])

film1.recensione()
film2.recensione()

    




    

            
        