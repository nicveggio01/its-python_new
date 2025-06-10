nome= input("inserire il nome: ")
ruolo= input("inserire il ruolo (admin, moderatore, utente, ospite): ")
eta=int(input("inserire l'età dell'utente: "))
if ruolo == "admin":
    print("accesso completo a tutte le funzionalità")
elif ruolo == "moderatore":
    print("puoi gestire i contenuti ma non modificare le impostazioni")
elif ruolo == "utente" and eta >= 18:
    print("accesso standard a tutti i servizi")
elif ruolo == "utente" and eta < 18:
    print("accesso limitato! alcune funzionalità sono bloccate")
elif ruolo == "ospite":
    print("accesso ristretto solo visualizzazione dei contenuti")
else:
    print("attenzione! ruolo non riconosciuto! accesso negato")
