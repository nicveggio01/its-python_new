

def cronometro(fun):
    def wrapped(*args):
        import time
        start= time.time()
        fun