current_users:list=["stefano", "lisa", "sara", "max", "giorgio"] 
new_users: list=["paola", "giovanni", "stefano", "sara", "francesca"] 

for i in new_users:
    if i in current_users:
        print("the username is already used, please choose another one!")
    
else:
    print("the username is not available")
          
current_users_upper =[user.upper() for user in current_users] 

for user in new_users:
    if user.upper() in current_users_upper:
        print(f"Nome utente '{user}' già in uso, scegline uno diverso.")
    else:
        print(f"il nome utente '{user}' è già disponibile")