import unittest
from apl import testing_print



class TestCase(unittest.TestCase):
    def test_pavadinimas_ir_laikas(self):
        pavadinimas1 = 'Microsoft Edge.lnk'
        laikas1 = '21:30'
        result = testing_print(pavadinimas1, laikas1)
        expected_result = 'Jūsų programa: Microsoft Edge.lnk bus įjungta 21:30.'
        self.assertEqual(result, expected_result)

    
    def test_pavadinimas(self):
        pavadinimas1 = 'Microsoft Edge.lnk'
        laikas1 = None
        result = testing_print(pavadinimas1, laikas1)
        expected_result = 'Jūsų programa: Microsoft Edge.lnk bus įjungta.'
        self.assertEqual(result, expected_result)


    def test_laikas(self):
        pavadinimas1 = None
        laikas1 = '21:30'
        result = testing_print(pavadinimas1, laikas1)
        expected_result = 'Įveskite programos pavadinimą.'
        self.assertEqual(result, expected_result)
    

    def test_be_pavadinimo_ir_laiko(self):
        pavadinimas1 = ''
        laikas1 = ''
        result = testing_print(pavadinimas1, laikas1)
        expected_result = 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
        self.assertEqual(result, expected_result)


    def test_integer(self):
        pavadinimas1 = 55
        laikas1 = '21:30'
        result = testing_print(pavadinimas1, laikas1)
        expected_result = 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
        self.assertEqual(result, expected_result)







unittest.main()