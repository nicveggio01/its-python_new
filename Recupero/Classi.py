
class ContactManager:

    def __init__(self, contacts: dict[str, list[str]]):
        self.contacts= contacts
    
    def create_contact(self, name: str, phone_numbers: list[str]):
        self.contacts[name]=phone_numbers

        if name in self.contacts:
            print("Errore il contatto esiste già.")
        else:
            self.contacts[name]=phone_numbers
    
    def add_phone_number(self, contact_name: str, phone_number: str):

        if contact_name in self.contacts:
            self.contacts[contact_name].append(phone_number)
        else:
            print("Errore il contatto non esiste")

        if phone_number in self.contacts[contact_name]:
            print("Errore il numero di telefono è già presente.")
        else:
            self.contacts[contact_name].append(phone_number)
        
    def remove_phone_number(self, contact_name: str, phone_number: str): 

        if contact_name in self.contacts:
            self.contacts[contact_name].remove(phone_number)
        else:
            print("Errore il contatto non esiste")

        if phone_number not in self.contacts:
            print("Il numero non è presente")
        else:
            self.contacts[contact_name].remove(phone_number)
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number:str):

        if contact_name in self.contacts:

            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
            else:
                print("Errore il numero di telefono non esiste")
        else:
            print("Errore il contatto non esiste")
        
    def list_phone_numbers(self, contact_name: str): 
        if contact_name not in self.contacts:
            print("Errore il contatto non è presente")
            return []
        return self.contacts[contact_name]
    
    def list_contacts(self)-> list[str]:
        return(self.contacts.keys())
    
    def search_contact_by_phone_number(self, phone_number: str):
         
        contatti=[]

        for name, numbers in self.contacts.items():
         
            if phone_number in numbers:
             
             contatti.append(name)
             return contatti
            
        if not contatti:    
            print("Nessun contatto trovato con questo numero di telefono")
        return contatti
             
             




        



