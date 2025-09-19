import time

class TimeManager:

    def __init__(self, file_name:str, mode:str):

        self._file_name=file_name
        self._mode=mode
        self._file= None
        self._start_time=None

    def __enter__(self):
        print("Resource adcquired ")
        self._file= open(self._file_name, self._mode, encoding="utf-8")
        self._start_time= time.time()

        return self._file
    
    def __exit__(self, exc_type, exc_value, traceback):

        if self._file:
            self._file.close()
            print("Resource Released")
        
        elapsed= time.time() - self._start_time
        print(f"Tempo trascorso: {elapsed} secondi")

        if exc_type is not None:
            
            print(f"Exception Type: {exc_type}")
            print(f"Exception Value: {exc_value}")
            print(f"Traceback: {traceback}")
        
        return False

with TimeManager("timer.txt", "w") as f:
    f.write("Inizio Timer")

            