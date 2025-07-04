

class Veicolo:

    _marca:str
    _modello:str
    _anno:int

    def __init__(self, marca:str, modello:str, anno:int):

        self._marca=marca
        self._modello= modello
        self._anno= anno
    
    def descrivi_veicolo(self):
        print(f"Marca: {self._marca}, Modello: {self._modello}, Anno: {self._anno}")
    

class Auto(Veicolo):
    _numero_porte:int
    def __init__(self, marca:str, modello:str, anno:int, numero_porte:int):
        super().__init__(marca=marca, modello= modello, anno=anno)

        if not numero_porte:
            print("Errore l'auto deve avere almeno una porta")
            return
        self._numero_porte=numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self._marca}, Modello: {self._modello}, Anno: {self._anno} ,Numero di Porte: {self._numero_porte}")
    
class Moto(Veicolo):
    _tipo:str

    def __init__(self, marca:str, modello:str, anno:int, tipo:str):
        super().__init__(marca=marca, modello=modello, anno= anno)

        if not tipo:
            print(f"Errore il tipo deve essere specificato")
            return
        self._tipo=tipo 
    
    def descrivi_veicolo(self):
        print(f"Marca: {self._marca}, Modello: {self._modello}, Anno: {self._anno}, Tipo: {self._tipo}")


veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto

