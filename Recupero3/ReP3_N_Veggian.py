from custom_types import RealGTZ
from typing import List
import random



class Creatura:

    _nome: str

    def __init__(self, nome: str):
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        if isinstance(nuovo_nome, str):
            self._nome = nuovo_nome
        else:
            self._nome="Creatura Generica"
    def __str__(self) -> str:
        return f"Creatura: {self._nome.upper()}"


class Alieno(Creatura):

    def __init__(self, nome: str):
        if not nome.startswith("Robot"):
            raise ValueError("Attenzione! Tutti gli Alieni devono avere il nome [Robot] seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()

    def __setMatricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)

    def get_matricola(self) -> RealGTZ:
        return self.__matricola

    def __setMunizioni(self) -> None:
        self.__munizioni:List[int]=[i**2 for i in range(15)]

    def get_munizioni(self) -> List[int]:
        return self.__munizioni

    def setMunizioni(self, nuova_lista: List[int]) -> None:
        if isinstance(nuova_lista, list) and len(nuova_lista) == 15 and all(isinstance(x, int) and x >= 0 for x in nuova_lista):
            self.__munizioni = nuova_lista
        else:
            raise ValueError("Lista non valida: devono essere 15 numeri positivi")

    def __str__(self) -> str:
        return f"Matricola: {self.__matricola}  +  Munizioni: {self.__munizioni}"


class Mostro(Creatura):

    __urlo_vittoria:str
    __gemito_sconfitta:str
    __assalto:list[int]

    def __init__(self, nome:str):

        nome_alternato= self.genera_nome_alternato(nome)

        super().__init__(nome_alternato)
        self.__setVittoria()
        self.__setSconfitta()
        self.__setAssalto()

    def genera_nome_alternato(self, nome:str)->str:
        new_name=""
        for i, c in enumerate(nome):
            if i%2==0:
                new_name+= c.upper()
            else:
                new_name+=c.lower()
        return new_name



    def __setAssalto(self)->None:
        self.__assalto= [random.randint(0,200) for _ in range(15)]


    def get_assalto(self)->list[int]:
        return self.__assalto
    def __setSconfitta(self)->None:
        self.__gemito_sconfitta= "Uuurghhh"
    def get_sconfitta(self)-> str:
        return self.__gemito_sconfitta
    def __setVittoria(self)->None:
        self.__urlo_vittoria="GRAAAHHH"
    def get_vittoria(self)->str:
        return self.__urlo_vittoria
    def __str__(self)-> str:
        return f"Mostro:{self._nome}"
    
 

def pariUguali(a: list[int], b: list[int])->list[int]:

    lunghezza_entrambe= min(len(a), len(b))

    c=[]

    for i in range(lunghezza_entrambe):
        if a[i]== b[i] and a[i] % 2==0:
            c.append(1)
        else:
            c.append(0)
    return c
        

def combattimento( a: Alieno, m: Mostro) -> Alieno | Mostro | None:

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore! Combattimento interrotto. Personaggi non validi.")
        return None
    else:
        result= pariUguali(a.get_munizioni(), m.get_assalto())

        conteggio=0
        for r in result:
            if r == 1:
                conteggio+= 1
            else:
                pass
            
        
        if conteggio > 4:
            print(f"Il vincitore del combattimento è {m.get_nome()}")
            print("--------")
            print(m.get_vittoria())
            return m
    
        else:
            print(f"Il vincitore del combattimento è l'alieno {a.get_nome()}")
            print("--------")
            print(m.get_sconfitta())
            return a

def proclamaVincitore(c:Creatura)-> None:

    larghezza= len(c.get_nome()) + 8
    bordo= "*"* larghezza
    vuoto= "*" +(""*(larghezza-2))+"*"
    centrale= "*   "+c.get_nome() +"   *" 
    return "\n".join([bordo, vuoto, centrale, vuoto, bordo])


def main():

    alieno= Alieno("Robot-256723")
    mostro=Mostro("GoDzIlLa")
    

    vincitore= combattimento(alieno, mostro)
    print()
    print(proclamaVincitore(vincitore))

if __name__ == "__main__":
    main()

