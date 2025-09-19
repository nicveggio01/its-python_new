
from persona import Persona

class Paziente(Persona):
    def __init__(self, nome, cognome, eta, id):
        super().__init__(nome=nome, cognome=cognome, eta=eta)

        if not isinstance(id, str):
            raise ValueError("L'ID non è una stringa")
        else:
            self._id=id
    
    def setIdCode(self, idCode:str):

        if not isinstance(idCode, str):
            raise ValueError("L'ID non è una stringa")
        else:
            self._id = idCode

    def getidCode(self)-> str:
        return self._id
    
    def patientInfo(self):
        print(f"Paziente:{self.nome} {self.cognome}\nID:{self._id}")
