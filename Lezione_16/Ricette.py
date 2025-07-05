class RecipeManager:

    def __init__(self):
        self._ricette = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> None:
        if name in self._ricette:
            return f"La ricetta esiste già"
        if not ingredients:
            return f"Ingredienti non trovati"
        self._ricette[name] = ingredients
        return self._ricette

    def add_ingredient(self, recipe_name: str, ingredient: str) -> None:
        if recipe_name not in self._ricette:
            return "Errore: la ricetta non esiste."
        if ingredient in self._ricette[recipe_name]:
            return f"Errore l'ingrediente {ingredient} esiste già"
        self._ricette[recipe_name].append(ingredient)
        return self._ricette

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> None:
        if recipe_name not in self._ricette:
            return f"Errore la ri cetta {recipe_name} non esiste."
        if ingredient not in self._ricette[recipe_name]:
            return f"Errore l'ingrediente {ingredient} non esiste quindi non può essere tolto."
        self._ricette[recipe_name].remove(ingredient)
        return self._ricette[recipe_name]

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]:
        if recipe_name not in self._ricette:
            return f"Ricetta {recipe_name} inesistente"
        if old_ingredient not in self._ricette[recipe_name]:
            return f"Errore: impossibile sostituire il vecchio ingrediente,{old_ingredient}, non esiste."
        indice_old = self._ricette[recipe_name].index(old_ingredient)
        self._ricette[recipe_name][indice_old] = new_ingredient
        return self._ricette[recipe_name]

    def list_recipes(self) -> list[str]:
        ricette=[]
        if not self._ricette:
            print("Nessuna ricetta presente.")
        for nome in self._ricette:
            ricette.append(nome)
        return ricette

    def list_ingredients(self, recipe_name: str) -> list[str]:
        if recipe_name not in self._ricette:
            print("Errore: ricetta inesistente!")
            return []
        return self._ricette[recipe_name]

    def search_recipe_by_ingredient(self, ingredient: str) -> dict[str, list[str]]:
        ricette = {}
        for nome, ingredienti in self._ricette.items():
            if ingredient in ingredienti:
                ricette[nome]=ingredienti
        if not ricette:
            print(f"Nessuna ricetta trovata con l'ingrediente '{ingredient}'.")
        return ricette


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

manager = RecipeManager()
print(manager.create_recipe("Spaghetti alla Carbonara", ["Spaghetti", "Uova", "Guanciale", "Pecorino Romano", "Pepe"]))
print(manager.search_recipe_by_ingredient("Uova"))
            
            

        
        
        

