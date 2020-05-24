import os


class TemporaryFile:
    def __init__(self, name):
        self.file = open(name, "w")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.file.name)


def verify(path):
    print("Is {} present?: {}.".format(path, os.path.exists(path)))


file_name = "test1.txt"

verify(file_name)

with TemporaryFile(file_name) as storage:
    print(storage.writable())
    verify(file_name)

verify(file_name)
