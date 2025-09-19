
from paziente import Paziente
from dottore import Dottore
from fatture import Fattura

d1= Dottore("Luca", "Bianchi", 34, "Pediatra", 80.00)
d2= Dottore("Mattia", "Mencarelli", 45, "Medico Generale", 50.70)

p1= Paziente("Sergio", "De guidi", 22, "01")
p2= Paziente("Claudio", "Benigni", 21, "02" )
p3= Paziente("Paola", "Geppi", 52, "03")
p4= Paziente("Giovanni", "Veggian", 51, "04")
p5= Paziente("Daniele", "Tafi", 40, "05")

dottori= [d1, d2]

for d in dottori:
    d.doctorGreet()

fattura1= Fattura([p1, p2, p3], d1)

fattura2= Fattura([p4], d2)

fatture= [fattura1, fattura2]

for f in fatture:
    print(f"Salario Dottor {f.doctor.cognome}: {f.getSalary()}")
    print("---------------------------")

fattura1.removePatient("02")
fattura2.addPatient(p2)

print(fattura1.getSalary())
print(fattura2.getSalary())


guadagno_ospedale=0

for f in fatture:
    guadagno_ospedale += f.getSalary()

print(f"In totale, l'ospedale ha incassato tot {guadagno_ospedale} euro")
