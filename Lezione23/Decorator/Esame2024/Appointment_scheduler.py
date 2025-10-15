
class AppointmentScheduler:

    def __init__(self, appointments:dict[str,dict]):
        self.appointments=appointments if appointments else {}
    
    def schedule_appointment(self, app_id:str, data:str)-> dict | str:
        if app_id in self.appointments:
            return f"Errore l'appuntamento {app_id} esiste già"
        else:
            self.appointments[app_id]= {"Data": data, "Programmato":True}
            return self.appointments
    
    def reschedule_appointment(self, app_id:str, nuova_data:str)-> dict|str:
        if app_id not in self.appointments:
            return f"Errore l'appuntamento {app_id} non esiste"
        else:
            self.appointments[app_id]={"Data":nuova_data, "Programmato":True}
            return f"APPUNTAMENTO RIPROGRAMMATO: {self.appointments[app_id]}"
    
    def cancel_appointment(self, app_id:str)-> dict | str:

        if app_id not in self.appointments:
            return f"Errore appuntamento {app_id} non trovato."
        else:
            self.appointments[app_id]["Programmato"]= False

            return self.appointments[app_id]
    
    def remove_appointment(self, app_id:str)-> dict|str:
        app_rimosso= {}
        if app_id not in self.appointments:
            return f"Errore appuntamento {app_id} non trovato"
        else:
            self.appointments.pop(app_id)
            app_rimosso = app_id
            
            return f"Id Appuntamento rimosso dall'agenda: {app_rimosso}"
    
    def list_appointments(self)-> list[str]:
        lista_app=[]

        for app_id in self.appointments:
            lista_app.append(app_id)
        
        return lista_app

    def get_appointment(self, app_id:str)-> dict|str:
        if app_id not in self.appointments:
            return f"Errore appuntamento {app_id} non trovato"
        else:
            return f"Appuntamento:{self.appointments[app_id]}"



scheduler= AppointmentScheduler({
    "A1":{"Data":"2025-10-22", "Programmato":True},
    "A2":{"Data":"2025-11-9", "Programmato":True},
    "A3":{"Data":"2025-10-26", "Programmato":False},
    "A4":{"Data":"2025-10-17", "Programmato":True}
})

print(scheduler.reschedule_appointment("A1", "2025-10-24"))
print(scheduler.get_appointment("A2"))
print(scheduler.list_appointments())
print(scheduler.remove_appointment("A4"))
print(scheduler.cancel_appointment("A2"))
print(scheduler.schedule_appointment("A5", "2025-10-30"))




    
