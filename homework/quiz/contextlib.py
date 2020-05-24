from contextlib import contextmanager

@contextmanager
def generator_function():
    yield "some value"

with generator_function() as value:
    print(value.upper())  # no PyCharm autocompletion
