from contextlib import contextmanager
import time


@contextmanager
def venloji_timer(name):
    start = time.time()
    yield
    print('[{0}] done in \t\t {1} s'.format(name, time.time() - start))
