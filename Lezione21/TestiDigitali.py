

class Documento:
    _testo: str

    def __init__(self, testo: str):
        self._testo = testo
    def getText(self) -> str:
        return self._testo
    def set_text(self, nuovo_testo: str):
        self._testo = nuovo_testo
    def isInitext(self, parola: str) -> bool:
        return parola in self._testo


class Email(Documento):
    _mittente: str
    _destinatario: str
    _titolo_messaggio: str

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(testo)
        self._mittente = mittente
        self._destinatario = destinatario
        self._titolo_messaggio = titolo_messaggio

    def get_mittente(self) -> str:
        return self._mittente

    def set_mittente(self, mittente: str) -> None:
        self._mittente = mittente

    def get_destinatario(self) -> str:
        return self._destinatario

    def set_destinatario(self, destinatario: str) -> None:
        self._destinatario = destinatario

    def getText(self) -> str:
        return f"Mittente: {self._mittente}\nDestinatario: {self._destinatario}\nTitolo Messaggio: {self._titolo_messaggio}\nMessaggio: {self._testo}"

    def writeToFile(self, nome_percorso: str) -> None:
        with open(nome_percorso, "w") as file:
            file.write(self.getText())


class File(Documento):
    _nomePercorso: str

    def __init__(self, testo: str, nomePercorso: str):
        super().__init__(testo)
        if not nomePercorso:
            raise ValueError("Errore: il nome del percorso deve essere specificato")
        self._nomePercorso = nomePercorso

    def get_nomePercorso(self) -> str:
        return self._nomePercorso

    def set_nomePercorso(self, nome_percorso: str):
        self._nomePercorso = nome_percorso

    def leggiTestoDaFile(self) -> str:
        with open(self._nomePercorso, "r") as reader:
            self._testo = reader.read()
            return self._testo

    def getText(self) -> str:
        self.leggiTestoDaFile()  
        return f"Percorso: {self._nomePercorso}\nContenuto: {self._testo}"


email1 = Email("Ciao Dome, possiamo incontrarci domani?", "Sergio.04@gmail.com", "dome87@gmail.com", "I garbati")

file1 = File("", "document.txt")

print(email1.getText())
print(file1.getText())
email1.writeToFile("email.txt")
print(email1.isInitext("incontrarci"))
file1.leggiTestoDaFile()
print(file1.isInitext("percorso"))







    




        
    





        

        
        
        

        