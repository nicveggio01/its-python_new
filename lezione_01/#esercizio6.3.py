#esercizio6.3

glossary:dict={"python": "Python è un linguaggio di programmazione ad alto livello, orientato a oggetti.", "ciclo": "è una struttura di controllo che permette di eseguire un blocco di codice più volte.", "data linker": "strumento o a una tecnologia che permette di collegare e gestire dati provenienti da fonti diverse o che operano su sistemi diversi.", "algoritmo": "In informatica, un algoritmo è una serie di istruzioni che definiscono un processo che un computer deve eseguire per arrivare a una soluzione o un risultato."} 

for word, definition in glossary.items():
    print(f"{word}'s definition is {definition}.  ")