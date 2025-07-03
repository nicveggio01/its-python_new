class Contatore:
    def __init__(self):
        self._conteggio = 0

    def setZero(self):
        self._conteggio = 0

    def add1(self):
        self._conteggio += 1

    def sub1(self):
        if self._conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self._conteggio -= 1

    def get(self):
        return self._conteggio

    def mostra(self):
        print(f"Conteggio attuale: {self._conteggio}")

        