def is_integer(valore):
    return isinstance(valore, int)
class Frazione:

    def __init__(self, numeratore:float | int, denominatore:float| int):

        self._numeratore= numeratore
        self._denominatore= denominatore
    
    def get_denominatore(self)-> float:
        return self._denominatore
    def set_denominatore(self, valore)-> None:
        if valore==0:
            self._denominatore= 5
        elif is_integer(valore):
            self._denominatore= valore
        else:
            self._denominatore=13
            
    def get_numeratore(self)-> float:
        return self._numeratore
    def set_numeratore(self, valore)-> None:
        if is_integer(valore):
            self._numeratore= valore
        else:
            self._numeratore= 5
    def value(self)-> float:
        result= round(self._numeratore/self._denominatore, 3)
        return result
    def __str__(self)->str:
        return f"{self._numeratore}/{self._denominatore}"

    # calcolo Massimo Comun divisore
    @staticmethod
    def mcd(x:int, y:int)-> int:

        divisori_comuni=[]
       

        valore_min= min(x, y)

        for i in range(1, valore_min+1):
                if x%i==0 and y%i==0:
                    divisori_comuni.append(i)
        if divisori_comuni:
            return max(divisori_comuni)
        else:
            return 1
        
    # Frazioni irriducibili: Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, ovvero il più grande divisore comune tra numeratore e denominatore è 1.


    def semplificata(self):
            
        if self._denominatore==0:
            raise ValueError("Errore non si può dividere un numero per 0.")
        else:
            divisore= Frazione.mcd(self._numeratore, self._denominatore)
            n=int(self._numeratore)
            d=int(self._denominatore)
            n_sempl= n//divisore
            d_sempl=d//divisore
        return Frazione(n_sempl, d_sempl)
    
    def é_irriducibile(self)-> bool:
        if Frazione.mcd(int(self._numeratore), int(self._denominatore))== 1:
            return True
        else:
            return False
        
    @staticmethod
    def semplifica(list_frazioni:list)->  list:

        irriducibili=[]

        for f in list_frazioni:
            if f.é_irriducibile():
                irriducibili.append(f)
            else:
                irriducibili.append(f.semplificata())
        
        return irriducibili
    
    def fractionCompare(self, lista_originale:list, lista_semplificata:list)-> None:

        for fraz_originale, fraz_semplificata in zip(lista_originale, lista_semplificata):

            val_originale= fraz_originale.value()
            val_semplificato= fraz_semplificata.value()

            # dimostrare che il valore della frazione originale è uguale al valore della frazione semplificata

            if val_originale== val_semplificato:

                print(f"Il valore della frazione originale:{val_originale}-----> Valore della frazione semplificata {val_semplificato}")
            else:
                print(f"Valori differenti:{val_originale} =! {val_semplificato}")








        



    









    
                

                    




    

    
    



    


