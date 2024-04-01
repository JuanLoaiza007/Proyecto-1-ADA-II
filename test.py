from models.types import *
from tests.test_correctitud_voraz import test_correctitud_voraz as test1
from tests.test_correctitud_dinamico import test_correctitud_dinamico as test2
from tests.test_correctitud import test_correctitud as test3
# from tests.test_correctitud import test_correctitud as test

if __name__ == '__main__':
    test1.start()
    test2.start()
    test3.start()
    # None
