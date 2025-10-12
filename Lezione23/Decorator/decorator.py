
def cronometro(fun):

    def wrapper(*args):
        import time
        start= time.time()
        fun(*args)
        print(time.time() - start)
    
    return wrapper

@cronometro
def prova():
    lista=[]
    for i in range(101):
        lista.append(i)
    print(lista)


prova()



