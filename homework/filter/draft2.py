import os


class FileManager:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        if os.path.exists(self.name):
            self.file = open(self.name, self.mode)
            return self.file
        else:
            print('Such a file does not exist.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    with FileManager('test_fil.txt', 'r') as open_file:
        if open_file:
            print(open_file.read())
        else:
            print("Please try again.")
