
from persona import Persona

class Dottore(Persona):
    def __init__(self, nome, cognome, eta, specializzazione, parcella):
        super().__init__(nome= nome, cognome= cognome, eta= eta)

        if not isinstance(specializzazione, str) or specializzazione not in ["Pediatra", "Ostetrico", "Medico Generale"]:
            self.specializzazione= None
            raise ValueError("Specializzazione deve essere una stringa")
        else:
            self.specializzazione= specializzazione


        if not isinstance(parcella, float):
            self.parcella= None
            raise ValueError("La parcella non è un float")
        
        else:
            self.parcella= parcella
    
    def setSpecialization(self, specialization:str):

        if not isinstance(specialization, str):
            raise ValueError("La specializzazione inserita non è una stringa")
        else:
            self.specializzazione= specialization
    
    def setParcel(self, parcel:float):

        if not isinstance(parcel, float):
            raise ValueError("La parcella inserita  on è un float")
        else:
            self.parcella= parcel
    
    def getSpecialization(self)-> str:
        return self.specializzazione
    
    def getParcel(self)-> float:
        return self.parcella
    
    def isAValidDoctor(self)-> bool:

        if self._eta > 30:
            print(f"Doctor {self.nome} {self.cognome} is valid!")
            return True
        
        else:
            print(f"Doctor {self.nome} {self.cognome}")
            return False

    def doctorGreet(self):
        print(f"Sono un medico {self.specializzazione}")


    