class FileManager:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode)
        except:
            print("Error.")
        finally:
            return self.file



    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')



if __name__ == "__main__":
    with FileManager("test_fidle.txt", "r") as open_file:
        print(open_file.read())
