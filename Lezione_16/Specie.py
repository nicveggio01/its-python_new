
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

        while popolazione_specie1 <= popolazione_specie2:

            popolazione_specie1 += int(popolazione_specie1*(self._tasso_crescita/100))
            popolazione_specie2 += int(popolazione_specie2* (altra_specie._tasso_crescita/100))
            anni +=1
        
        return anni
    
    def getDensita(self, area_kmq: float) -> int:
        anni = 0
        popolazione = self._popolazione  

        while (popolazione / area_kmq) < 1:
            popolazione += popolazione * (self._tasso_crescita / 100)
            anni += 1
        return anni

class BufaloKlingon(Specie):

    def __init__(self, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__("Bufalo Klingon", popolazione_iniziale= popolazione_iniziale, tasso_crescita= tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione_iniziale:int, tasso_crescita:float):
        super().__init__("Elefante", popolazione_iniziale= popolazione_iniziale, tasso_crescita= tasso_crescita)

bufalo_klingon = BufaloKlingon(100, 15)  
elefante = Elefante(10, 35)  


anni_necessari = elefante.anni_per_superare(bufalo_klingon)  
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")


anni_densita = bufalo_klingon.getDensita(1500) 
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")









