import unittest
from helpers import *

# Remove if no python functions are not tested
#from my_code import *  # Jatetty tarkoituksella tässä tapauksessa

# HUOM! Tuo yllä oleva rivi ajaa my_code.py:n ja siellä tehdyt muuttujat jäävät
#      globaaleiksi muuttujiksi. test_Python-metodissa my_code.py:tä ei enää
#      ajeta, vaan siellä tarkastetaan vain vaaaditut globaalit muuttujat.


started_tests = 0
completed_tests = 0


class TestCode(unittest.TestCase):

    def test_Python(self):
        # Test python program
        self.startTest()

        # Ajetaan sitten ohjelma uudelleen ja katsotaan mitä se kirjoittaa stdoutiin
        results = callpython(cmdline_args=[], input='-31\n').strip()

        expected_results = ['kylmä']

        for r in expected_results:
            print('Is ' + r + ' in output?')
            self.assertTrue(r in results)

        results = callpython(cmdline_args=[], input='-2\n').strip()

        expected_results = ['Pakkasta']

        for r in expected_results:
            print('Is ' + r + ' in output?')
            self.assertTrue(r in results)

        results = callpython(cmdline_args=[], input='0\n').strip()

        expected_results = ['Haaleaa']

        for r in expected_results:
            print('Is ' + r + ' in output?')
            self.assertTrue(r in results)

        results = callpython(cmdline_args=[], input='12\n').strip()

        expected_results = ['Lämmintä']

        for r in expected_results:
            print('Is ' + r + ' in output?')
            self.assertTrue(r in results)

        results = callpython(cmdline_args=[], input='39.2\n').strip()
        expected_results = ['kuuma']

        results = callpython(cmdline_args=[], input='38.9\n').strip()
        expected_results = ['Lämmintä']

        for r in expected_results:
            print('Is ' + r + ' in output?')
            self.assertTrue(r in results)

        mycode = loadmycode()

        print(mycode)
        self.assertTrue(mycode.count('if ')+mycode.count('if(') >= 1)
        self.assertTrue(mycode.count('elif ')+mycode.count('elif(') >= 1) 
        self.assertTrue(mycode.count('else') >= 1)
        #self.assertTrue(mycode.count('float') >= 1) #Ei tarvita. Jos 39.2 ja 38.9 toimii, niin silloin on oikea tyyppi

        self.endTest()

    def startTest(self):
        global started_tests
        started_tests = started_tests + 1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests = completed_tests + 1


def completed():
    global completed_tests
    return completed_tests


def started():
    global started_tests
    return started_tests