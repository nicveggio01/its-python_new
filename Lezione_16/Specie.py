
class Specie:

    def __init__(self, nome:str, popolazione_iniziale: int, tasso_crescita:float):

        self._nome=nome
        self._popolazione=popolazione_iniziale
        self._tasso_crescita=tasso_crescita

    def cresci(self):
        self._popolazione += int(self._popolazione* (self._tasso_crescita/100))
    
    def anni_per_superare(self, altra_specie:'Specie')->int:
        
        anni=0
        popolazione_specie1= self._popolazione
        popolazione_specie2= altra_specie._popolazione

        while popolazione_specie2 <= popolazione_specie1:

            popolazione_specie1 += (popolazione_specie1*(self._tasso_crescita/100))
            popolazione_specie2 += (popolazione_specie2* (altra_specie._tasso_crescita/100))
            anni +=1
        
        return anni
    
    def getDensita(self, area_kmq:float)->int:
        anni=0

        while self._popolazione/area_kmq < 1:
            self._popolazione += (self._popolazione*(self._tasso_crescita/100))
            anni +=1
        return anni

class BufaloKlingon(Specie):

    def __init__(self, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__("Bufalo Klingon", popolazione_iniziale= popolazione_iniziale, tasso_crescita= tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__("Elefante", popolazione_iniziale= popolazione_iniziale, tasso_crescita= tasso_crescita)



# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")









