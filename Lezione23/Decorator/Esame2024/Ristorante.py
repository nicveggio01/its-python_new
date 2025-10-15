
class Table:

    def __init__(self, table_id:str, capacity:int, is_reserved:bool= False):

        self.table_id= table_id
        if capacity <=0:
            raise ValueError("La capacità del tavolo non può essere minore o uguale di 0")
        else:
            self.capacity= capacity
        
        self.is_reserved= is_reserved
    
    def reserve(self)-> None:

        if self.is_reserved==False:
            self.is_reserved= True
        else:
            print(f"Il tavolo {self.table_id} è già riservato")
    
    def cancel_reservation(self)-> None:
        if self.is_reserved==True:
            self.is_reserved= False
        else:
            print(f"Il tavolo {self.table_id} non è stato riservato")

class Customer:

    def __init__(self, customer_id:str, name:str, reserved_tables:list[Table]= []):
        self.customer_id= customer_id
        self.name= name
        self.reserved_tables= reserved_tables if reserved_tables else []

    
    def reserve_table(self, table:Table)-> None:

        if table.is_reserved==False:
            table.is_reserved=True
            self.reserved_tables.append(table)
        else:
            print(f"Il tavolo {table.table_id} non è disponibile")
    
    def cancel_table(self, table:Table)-> None:

        if table in self.reserved_tables:
            table.is_reserved=False
            self.reserved_tables.remove(table)
        else:
            print(f"Il tavolo {table.table_id} non è stato prenotato da questo cliente")


class Restaurant:

    def __init__(self, tables:dict[str, Table], customers:dict[str, Customer]):
        self.tables= tables if tables else {}
        self.customers= customers if customers else {}
    
    def add_table(self, table_id:str, capacity:int)->None:
        if table_id in self.tables:
            print(f"Il tavolo con ID {table_id} esiste già")
        else:
            table= Table(table_id, capacity)
            self.tables[table_id]= table
    
    def register_customer(self, customer_id:str, name:str)-> None:
        if customer_id in self.customers:
            print(f"Cliente con ID {customer_id} già registrato")
        else:
            customer= Customer(customer_id, name)
            self.customers[customer_id]= customer
    
    def reserve_table(self, customer_id:str, table_id:str)-> None:
        if customer_id in self.customers and table_id in self.tables:
            self.customers[customer_id].reserve_table(self.tables[table_id])
        else:
            print(f"Cliente o tavolo non trovato")
    
    def cancel_table(self, customer_id:str, table_id:str)-> None:
        if customer_id in self.customers and table_id in self.tables:
            self.customers[customer_id].cancel_table(self.tables[table_id])
        else:
            print(f"Cliente o tavolo non trovato")
    
    def list_available(self)-> list[str]:
        list_available=[]
        for table in self.tables.values():
            if table.is_reserved== False:
                list_available.append(table)
            else:
                pass
        
        return list_available
    

    def list_customer_reservations(self, customer_id:str)-> list[str]|str:

        if customer_id in self.customers:
            return self.customers[customer_id].reserved_tables.table_id
        else:
            print(f"Errore cliente non trovato")

