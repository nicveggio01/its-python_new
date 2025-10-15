
class LibraryManager:

    def __init__(self, books:dict[str, dict]):
        self.books= books if books else {}
    
    def add_book(self, book_id:str, title:str, author:str)-> dict|str:
        if book_id in self.books:
            return f"Il libro esiste già"
        else:
            if self.books[book_id]["available"]==True:
                self.books[book_id]= {"title": title, "author":author}
                return {book_id: self.books[book_id]}
            else:
                return f"IL libro non è disponibile."
    
    def borrow_book(self, book_id:str)-> dict|str:

        if book_id not in self.books:
            return f"Errore libro non trovato"
        else:
            if self.books[book_id]["available"]==False:
                return f"Errore libro non disponibile"
            else:
                self.books[book_id]["available"]= False
                return {book_id: self.books[book_id]}
    
    def return_book(self, book_id:str)-> dict|str:

        if book_id not in self.books:
            return f"Errore libro non trovato"
        else:
            if self.books[book_id]["available"]==False:
                self.books[book_id]["available"]=True
                return {book_id: self.books[book_id]}
            else:
                return f"Il libro {book_id} è già stato arrestato."
    
    def remove_book(self, book_id:str) -> dict | str:

        book_remove= {}
        if book_id not in self.books:
            return f"Errore libro non trovato."
        else:
            libro_rimosso= self.books.pop(book_id)
            book_remove= libro_rimosso

            return {"book_id:", book_remove}
    
    def list_books(self)-> list[str]:
        list_book=[]
        for book in self.books.keys():
            list_book.append(book)
        return list_book
    
    def get_book(self, book_id:str)-> dict|str:

        if book_id not in self.books:
            return f"Libro non trovato"
        else:
            return {book_id: self.books[book_id]}
            
            
    
