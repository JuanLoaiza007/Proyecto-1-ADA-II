from models.types import *
from tests.test_correctitud_voraz import test_correctitud_voraz as test_voraz
from tests.test_correctitud_dinamico import test_correctitud_dinamico as test_dinamico_chebas
from tests.test_correctitud_juan_aerodinamico import test_correctitud_juan_aerodinamico as test_dinamico_juan
from tests.test_correctitud_exhaustiva import test_correctitud as test_exhaustiva

# from tests.test_correctitud import test_correctitud as test

if __name__ == '__main__':
    # test_voraz.start()
    # test_dinamico_chebas.start()
    # test_exhaustiva.start()
    test_dinamico_juan.start()
