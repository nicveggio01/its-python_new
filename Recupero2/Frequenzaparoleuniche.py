
import  string

def conta_parole_uniche(testo:str)-> dict:

    conteggio={}
    

    tokens= testo.split()

    
    for token in tokens:

        token= token.lower()

        token= token.strip(string.punctuation)
    
        if token== "":
            continue
        
        else:
            if token not in conteggio:
                conteggio[token]=0
            conteggio[token]+=1
            
    

    return conteggio
  
print(conta_parole_uniche("ciao ciao come stai?"))



