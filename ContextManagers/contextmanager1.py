class FileManager:
    def __init__(self, file_name:str, mode:str):
        self._file_name=file_name
        self._mode= mode
        self._file=None
    
    def __enter__(self):
        print("Resource acquired")
        self._file= open(self._file_name, self._mode, encoding= "utf-8")
        return self._file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self._file:
            self._file.close()
        print("Resource released")
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception Value: {exc_value}")
            print(f"Traceback: {traceback}")
        
        return False

with FileManager ('example.txt', 'w+') as f:
    f.write("Hello world I'm Nic")
    f.seek(0)
    print(f.read())


