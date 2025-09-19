
class Persona:
    def __init__(self, nome:str,cognome:str, eta:int=0):

        if not isinstance(nome, str):
            self.nome= None
            raise ValueError("Il nome inserito non è una stringa!")
        else:
            self.nome= nome
        
        if not isinstance(cognome, str):
            self.cognome= None
            raise ValueError("Il cognome non è una stringa")
        else:
            self.cognome= cognome
        
        if not isinstance(eta, int) or eta < 0:
                raise ValueError("L'età deve essere un intero non negativo")
        self._eta = eta
        
    def setName(self, first_name:str):

        if not isinstance(first_name, str):
            raise ValueError("First Name non è una stringa")
        else:
            self.nome= first_name
    
    def setLastName(self, last_name:str):

        if not isinstance(last_name, str):
            raise ValueError("Il cognome inserito non è una stringa")
        else:
            self.cognome= last_name

    def setAge(self, age:int):
        if not isinstance(age, int):
            raise ValueError("L'età deve essere un intero")
        else:
            self._eta= age
    
    def getName(self)-> str:
        return self.nome
    
    def getLastName(self) -> str:
        return self.cognome
    
    def greet(self)->str:
        print(f"Ciao sono {self.nome} {self.cognome}! Ho {self._eta} anni")
    

    

    
    

