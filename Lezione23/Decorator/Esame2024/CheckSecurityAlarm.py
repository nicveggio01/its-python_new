
'''Scrivi una funzione che verifica se una combinazione di sensori (S1, S2, S3) attiva l'allarme.
L'allarme si attiva solo se S1 è vero e (S2 o S3 è falso). La funzione deve ritornare "Allarme
attivato" oppure "Nessun allarme" a seconda delle condizioni.'''






def check_security_alarm(s1:bool, s2:bool, s3:bool)-> str:
    if s1==True and (s2==False or s3==False):
        return "Allarme attivato"
    else:
        return f"Nessun allarme attivato"