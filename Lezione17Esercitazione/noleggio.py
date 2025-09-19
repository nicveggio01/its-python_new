class Film:
    def __init__(self, id:int, titolo:str):
        self._id = id
        self._titolo = titolo
    
    def setId(self, new_id:int):
        self._id = new_id
    
    def setTitle(self, title:str):
        self._titolo = title
    
    def getId(self) -> int:
        return self._id
    
    def getTitle(self) -> str:
        return self._titolo
    
    def isEqual(self, otherFilm:'Film') -> bool:
        return self.getId() == otherFilm.getId()

class Azione(Film):
    def __init__(self, id, titolo):
        super().__init__(id=id, titolo=titolo)
        self.__penale = 3.0
        self.__genere = "Azione"

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, ritardo:int) -> float:
        return ritardo * self.getPenale()


class Commedia(Film):
    def __init__(self, id, titolo):
        super().__init__(id=id, titolo=titolo)
        self.__penale = 2.5
        self.__genere = "Commedia"

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, ritardo:int) -> float:
        return ritardo * self.getPenale()


class Drama(Film):
    def __init__(self, id, titolo):
        super().__init__(id=id, titolo=titolo)
        self.__penale = 2.0
        self.__genere = "Drama"
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, ritardo:int) -> float:
        return ritardo * self.getPenale()
    
class Noleggio:
    def __init__(self, film_list:list[Film]):
        self.film_list = film_list
        self.rented_film: dict[int, list[Film]] = {}
    
    def isAvailable(self, film:Film) -> bool:
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}")
            return False
    
    def rentAMovie(self, film:Film, clientID:int):
        if film not in self.film_list:
            print(f"Non è possibile noleggiare il film {film.getTitle()}")
            return
        self.film_list.remove(film)
        if clientID not in self.rented_film:
            self.rented_film[clientID] = []
        self.rented_film[clientID].append(film)
        print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}")
    
    def giveBack(self, film:Film, clientID:int, days:int):
        if clientID not in self.rented_film or film not in self.rented_film[clientID]:
            print(f"Errore: Il film {film.getTitle()} non è stato noleggiato da {clientID}")
            return
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)
        penale = film.calcolaPenaleRitardo(days)
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro")
    
    def printmovies(self):

        if not self.film_list:
            print("Nessun film disponibile in negozio")
        else:

            for f in self.film_list:
                print(f"{f.getTitle()}---{f.getGenere()}")
