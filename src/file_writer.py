from contextlib import contextmanager
import sys

@contextmanager
def open_file(filename):
    if filename != 'STDOUT':
        with open(filename, 'w') as f:
            yield f
    else:
        yield sys.stdout
