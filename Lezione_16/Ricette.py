
class RecipeManager:

    def __init__(self):
        self._ricette={}

    def create_recipe(self, name:str, ingredients:list[str])-> dict[str, list[str]]:

        if name in self._ricette:
            print("Errore la ricetta esiste già.")
            return
        if not ingredients:
            print("Non esiste una ricetta senza ingredienti.")
        else:
            self._ricette[name]= ingredients
    def add_ingredient(self, recipe_name:str, ingredient:str)-> dict[str, list[str]]|None:
        if not recipe_name in self._ricette:
            print("Errore la ricetta non esiste")
            return None
        if ingredient in recipe_name:
            print("Errore l'ingrediente esiste già")
            return None
        
        self._ricette[recipe_name].append(ingredient)
        return self._ricette
    
    def remove_ingredient(self, recipe_name, ingredient):
        if not recipe_name in self._ricette:
            print("Errore la ricetta non esiste.")
        if ingredient not in self._ricette[recipe_name]:
            print("Errore l'ingrediente non è esiste quindi non può essere tolto.")

        self._ricette[recipe_name].remove(ingredient)
    
    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str)-> dict[str, list[str]]:
        if not recipe_name in self._ricette:
            print("Errore la ricetta non esiste.")
            return
        if not old_ingredient in self._ricette[recipe_name]:
            print("Errore impossibile sostituire il vecchio ingrediente, non esiste.")
            return

        self._ricette[recipe_name].remove(old_ingredient)
        self._ricette[recipe_name].append(new_ingredient)
        return self._ricette[recipe_name]

    def list_recipes(self):
        if not self._ricette:
            print("Nessuna ricetta presente.")
        return self._ricette
    def list_ingredients(self, recipe_name:str)->list[str]:
        ingredienti=[]
        if not recipe_name:
            print("Errore ricetta inesistente!")
        for ingrediente in self._ricette.items():
            ingredienti.append(ingrediente)
        return ingredienti
    def search_recipe_by_ingredient(self, ingredient:str)-> list[str]:

        ricette=[]

        for nome, ingredienti in self._ricette.items():
            if ingredient in ingredienti:
                ricette.append(nome)
                return
            else:
                print("Nesuna ricetta esistente con tale ingrediente")
                return
            
            

        
        
        

