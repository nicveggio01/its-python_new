
'''data una lista di numeri,
ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota, solleva
un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
built-in di python o librerie.calculate_std_dev(nums: list[float]) -> float che, data una lista di
numeri, ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota,
solleva un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
built-in di python o librerie.
Nota Bene: Il calcolo della varianza misura la dispersione dei dati rispetto alla media. Si
calcola come la media dei quadrati delle differenze tra ciascun valore all’interno della lista e
la media dei valori della lista di numeri'''





def calculate_std_dev(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Lista vuota")
    else:
        somma=0
        for n in nums:
            somma += n
        media= somma/len(nums)

        somma_diff_quadrati=0

        for n in nums:
            diff= n-media
            somma_diff_quadrati += diff*diff
            varianza= somma_diff_quadrati/len(nums)
        
        deviazione_standard= varianza**0.5

        return deviazione_standard

print(calculate_std_dev([1.0, 2.0, 3.0, 4.0, 5.0]))
        

