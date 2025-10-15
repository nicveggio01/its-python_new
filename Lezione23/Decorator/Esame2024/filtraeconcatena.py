# prenda una lista di interi e un valore minimo, e restituisci una stringa concatenata di tutti i numeri di nums 
# che sono maggiori di min_val, separati da virgola (es. "5,7,9")

def filter_and_concat(nums: list[int], min_val: int) -> str:
    stringa=""

    for n in nums:
        if n > min_val:
            stringa += (str(n)+",")
        else:
            pass
    
    return stringa.rstrip(",")

print(filter_and_concat([10, 346, 2, 89, 76, 899, 1200, 5], 200))

