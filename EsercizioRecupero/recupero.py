
class TaskManager:
    def __init__(self, tasks:dict[str, dict[str, str|bool]]):
        self.tasks:dict[str, dict[str, str | bool]]= tasks
    
    def create_task(self, task_id:str, descrizione:str):

        if task_id in self.tasks:
            return f"Task Id {task_id} esite già"
        else:
            self.tasks[task_id] += descrizione

            return task_id[descrizione]
    
    def complete_task(self, task_id:str)-> dict[str, str|bool] | str:
        
        if task_id in self.tasks:
            self.tasks[task_id]["completato"]=True
            return f" task_id: {self.tasks[task_id]}"

        else: 
            return "chiave non presente!"
    
    def update_descr(self, task_id:str, descrizione:str) -> dict[str, dict[str, str | bool]]:

        if task_id not in self.tasks:
            return "Task non presente"
        else:
            self.tasks[task_id]["descrizione"]= descrizione
            return {task_id: {self.tasks[task_id]}}
        
    def remove_task(self, task_id:str) -> dict | str:
        if task_id not in self.tasks:
            return "Task non presente"
        else:
            value= self.tasks.pop(task_id)

            return {task_id: value}
    
    def list_tasks(self)-> list[str]:
        keys:list[str]= [key for key in self.tasks.keys()]
        return list(self.tasks.keys())
    
    def get_task(self, task_id:str)-> dict | str:
        if task_id not in self.tasks:
            return "Errore tasks non presente"
        else:
            return {task_id: self.tasks[task_id]}
    




