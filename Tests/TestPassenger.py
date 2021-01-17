'''
Created on Dec 12, 2019

@author: PAnita
'''
import unittest
from Domain.Passenger import Passenger


class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.__passenger=Passenger('Ana','Pop',5563525)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_getters(self):
        self.assertEqual(self.__passenger.getFirstName(), 'Ana')
        self.assertEqual(self.__passenger.getLastName(),'Pop')
        self.assertEqual(self.__passenger.getPassport(), 5563525)
        
    def test_setters(self):
        self.__passenger.setFirstName('Maria')
        self.assertEqual(self.__passenger.getFirstName(), 'Maria')
        
        self.__passenger.setLastName('Balogh')
        self.assertEqual(self.__passenger.getLastName(),'Balogh')
        
        self.__passenger.setPassport(299663)
        self.assertEqual(self.__passenger.getPassport(), 299663)
        
    def test_raises_setters(self):
        self.assertRaises(TypeError, lambda:self.__passenger.setPassport('99stt9'))
        self.assertRaises(TypeError, lambda:self.__passenger.setPassport('-9956'))

        