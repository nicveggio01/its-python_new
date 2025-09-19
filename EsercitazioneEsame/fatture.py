
from paziente import Paziente
from dottore import Dottore


class Fattura:
    def __init__(self, patient:list[Paziente], doctor:Dottore):

        if doctor.isAValidDoctor():
            self.fatture= len(patient)
            self.salary=0
            self.doctor=doctor
            self.patient=patient
        else:
            self.patient= None
            self.doctor=None
            self.fatture=None
            self.salary=None
            raise ValueError("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self)-> int|float:
        return self.doctor.getParcel() * len(self.patient)
    
    def getFatture(self)-> int:
        return self.fatture
    
    def addPatient(self, newPatient:Paziente):
        if newPatient in self.patient:
            raise ValueError("il pazienten è già nella lista dei pazienti.")
        else:
            self.patient.append(newPatient)
            self.fatture = len(self.patient)
            self.salary = self.doctor.getParcel() * len(self.patient)
            print(f"Alla lista  del Dottore {self.doctor.cognome} è stato aggiunto paziente {newPatient._id}")

    def removePatient(self, idCode):

        for p in self.patient:
            if p._id == idCode:
                self.patient.remove(p)
                self.fatture = len(self.patient)
                self.salary = self.doctor.getParcel() * len(self.patient)
                print(f"Alla lista del Dottor {self.doctor.cognome} è stato rimosso il paziente {idCode}")
            else:
                pass


