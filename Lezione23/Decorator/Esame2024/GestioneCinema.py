
class Ticket:
    def __init__(self, ticket_id:str, movie:str, seat:str, is_booked:bool):

        self.ticket_id= ticket_id
        self.movie= movie
        self.seat= seat
        self.is_booked= is_booked
    
    def book(self)-> None:
        if self.is_booked==False:
            self.is_booked=True
        else:
            print(f"Il biglietto per {self.movie} posto:{self.seat} è già prenotato")

    def cancel(self)-> None:
        if self.is_booked==True:
            self.is_booked= False
        else:
            print(f"Il biglietto per {self.movie}, posto:{self.seat} non risulta prenotato")


class Viewer:
    def __init__(self, viewer_id:str, name:str, booked_tickets:list[Ticket]=None):

        self.viewer_id= viewer_id
        self.name= name
        self.booked_tickets= booked_tickets if booked_tickets else []

    def book_ticket(self, ticket:Ticket)-> None:
        if ticket.is_booked==False:
            ticket.is_booked=True
            self.booked_tickets.append(ticket)
        else:
            print(f"Il biglietto per {ticket.movie} non è disponibile")
    
    def cancel_ticket(self, ticket:Ticket)-> None:
        if ticket in self.booked_tickets:
            ticket.is_booked=False
            self.booked_tickets.remove(ticket)
        else:
            print(f"IL biglietto per {ticket.movie} non è stato prenotato da questo spettatore.")

class Cinema:

    def __init__(self, tickets:dict[str, Ticket], viewers:dict[str, Viewer]):

        self.tickets= tickets if tickets else {}
        self.viewers= viewers if viewers else {}
    
    def add_ticket(self, ticket_id:str, movie:str, seat:str, is_booked:bool)-> None:

        if ticket_id in self.tickets:
            print(f"Il biglietto con {ticket_id} esiste già.")
        else:
            ticket= Ticket(ticket_id, movie, seat, is_booked)
            self.tickets[ticket_id]= ticket
    
    def register_viewer(self, viewer_id:str, name:str)-> None:
        if viewer_id in self.viewers:
            print(f"Lo spettatore con {viewer_id} esiste già")
        else:
            viewer= Viewer(viewer_id, name)
            self.viewers[viewer_id]= viewer
    
    def book_ticket(self, viewer_id:str, ticket_id:str)-> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            viewer= self.viewers[viewer_id]
            ticket= self.tickets[ticket_id]
            viewer.book_ticket(ticket)
        else:
            print(f"Spettatore {viewer_id} non trovato o biglietto {ticket_id} non trovato")
    
    def cancel_ticket(self, viewer_id:str, ticket_id:str)-> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            viewer= self.viewers[viewer_id]
            ticket=self.tickets[ticket_id]
            viewer.cancel_ticket(ticket)
        else:
            print(f"Spettatore {viewer_id} non trovato o biglietto {ticket_id} non trovato ")

    def list_available_tickets(self)-> list[str]:
        
        list_available=[]

        for ticket in self.tickets.values():
            if ticket.is_booked==False:
                list_available.append(ticket.ticket_id)
        
        return list_available
    
    def list_viewer_bookings(self, viewer_id:str)-> list[str]|str:

        list_bookings=[]

        if viewer_id not in self.viewers:
            return f"Lo spettatore {viewer_id} non esiste"
        else:
            viewer= self.viewers[viewer_id]
            return [ticket.ticket_id for ticket in viewer.booked_tickets]
        
    def get_viewers(self)->str:
        return self.viewers.values()
        
    


####################################################################################################


t1= Ticket("t1", "Titanic", "10A", True)
t2= Ticket("t2", "Titanic", "10B", True)
t3= Ticket("t3", "Titanic", "5F", True)
t4= Ticket("t4", "Titanic", "7A", False)
t5= Ticket("t5", "Titanic", "6F", False)
t6= Ticket("t6", "Weapons", "12N", True)
t7= Ticket("t7", "Weapons", "13N", True)
t8= Ticket("t8", "Weapons", "10N", False)
t9= Ticket("t9", "Weapons", "9N", False)
t10= Ticket("t10", "Weapons", "6N", False)

v1= Viewer("v1", "Niccolò", [t6, t7])
v2= Viewer("v2", "Domenico", [t1, t2, t3])

cinema = Cinema(
    tickets={
        "t1": t1, "t2": t2, "t3": t3, "t4": t4, "t5": t5,
        "t6": t6, "t7": t7, "t8": t8, "t9": t9, "t10": t10
    },
    viewers={
        "v1": v1,
        "v2": v2
    }
)




print(cinema.list_available_tickets())
print(cinema.list_viewer_bookings("v1"))
print(cinema.list_viewer_bookings("v2"))





    
