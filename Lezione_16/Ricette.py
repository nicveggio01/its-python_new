class RecipeManager:

    def __init__(self):
        self._ricette = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> None:
        if name in self._ricette:
            print("Errore: la ricetta esiste già.")
            return
        if not ingredients:
            print("Errore: non esiste una ricetta senza ingredienti.")
            return
        self._ricette[name] = ingredients

    def add_ingredient(self, recipe_name: str, ingredient: str) -> None:
        if recipe_name not in self._ricette:
            print("Errore: la ricetta non esiste.")
            return
        if ingredient in self._ricette[recipe_name]:
            print("Errore: l'ingrediente esiste già.")
            return
        self._ricette[recipe_name].append(ingredient)

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> None:
        if recipe_name not in self._ricette:
            print("Errore: la ricetta non esiste.")
            return
        if ingredient not in self._ricette[recipe_name]:
            print("Errore: l'ingrediente non esiste quindi non può essere tolto.")
            return
        self._ricette[recipe_name].remove(ingredient)

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]:
        if recipe_name not in self._ricette:
            print("Errore: la ricetta non esiste.")
            return
        if old_ingredient not in self._ricette[recipe_name]:
            print("Errore: impossibile sostituire il vecchio ingrediente, non esiste.")
            return
        indice_old = self._ricette[recipe_name].index(old_ingredient)
        self._ricette[recipe_name][indice_old] = new_ingredient
        return self._ricette[recipe_name]

    def list_recipes(self) -> dict[str, list[str]]:
        if not self._ricette:
            print("Nessuna ricetta presente.")
        return self._ricette

    def list_ingredients(self, recipe_name: str) -> list[str]:
        if recipe_name not in self._ricette:
            print("Errore: ricetta inesistente!")
            return []
        return self._ricette[recipe_name]

    def search_recipe_by_ingredient(self, ingredient: str) -> list[str]:
        ricette = [nome for nome, ingredienti in self._ricette.items() if ingredient in ingredienti]
        if not ricette:
            print("Nessuna ricetta esistente con tale ingrediente.")
        return ricette


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
            
            

        
        
        

