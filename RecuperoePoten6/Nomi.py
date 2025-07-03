
nomi=[]

nome_max=""

while len(nomi)< 30:
    nome= str(input("Inserisci un nome: "))

    if len(nome)==0:
        print("Non può essere inserito una stringa vuota.")
        continue
    if nome in nomi:
        print("Nome già inserito.Stop!")
        break
    if len(nome) >= 20:
        print("Nome troppo lungo.Stop!")
        break
 
    nomi.append(nome)

for nome in nomi:
    if len(nome) >len(nome_max):
        nome_max=nome



print(f"Sono stati inseriti {len(nomi)} nomi")
print(f"Il nome più lungo inserito è: {nome_max}")
print(f"lunghezza nome più lungo: {len(nome_max)}")






