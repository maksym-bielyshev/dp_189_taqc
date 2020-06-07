import time

class Timer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        # time.monotonic() requires Python >= 3.3
        self._start = time.monotonic()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print('Failed: {}: {}'.format(self._msg, exc_value))
        else:
            print('{}: {} s'.format(self._msg, time.monotonic() - self._start))


with Timer("doing stuff"):
    for i in range(1000000):
        pass

