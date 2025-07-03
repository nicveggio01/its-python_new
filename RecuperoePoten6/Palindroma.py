
def recursivePalindrome(testo:str)->bool:

    testo= testo.replace(" ", "")
    testo=testo.lower()

    if not testo:
        return True 
    elif len(testo) <=1:
        return True
    if testo[0] != testo[-1]:
        return False
    return recursivePalindrome(testo[1:-1])

testo= "Radar"
print(recursivePalindrome(testo))

