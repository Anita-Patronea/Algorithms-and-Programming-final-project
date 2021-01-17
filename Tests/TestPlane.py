'''
Created on Dec 12, 2019

@author: PAnita
'''
import unittest
from Domain.Plane import Plane
from Domain.Passenger import Passenger

class TestPlane(unittest.TestCase):
    
    def setUp(self):
        passenger1=Passenger('Ana','Pop',5563525)
        passenger2=Passenger('Andreea','Mare',55695145)
        passenger3=Passenger('Andrei','Paunescu',6355985)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        passenger5=Passenger('Marius','Faur',225296)
        
        list1=[passenger1,passenger2,passenger4]
        list2=[passenger3,passenger5,passenger4]
        
        self.__plane1=Plane("Ak-44", "WizzAir", 55, "Paris", list1)
        self.__plane2=Plane("233322", "BlueAir", 122, "Monaco", list2)
     
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_getters(self):
        self.assertEqual(self.__plane1.getName(), 'Ak-44')
        self.assertEqual(self.__plane1.getAirlineCompany(), 'WizzAir')
        self.assertEqual(self.__plane1.getNumberSeats(), 55)
        self.assertEqual(self.__plane1.getDestination(), 'Paris')
        self.assertEqual(self.__plane1.getListPassengers(), [Passenger('Ana','Pop',5563525),Passenger('Andreea','Mare',55695145),Passenger('Bogdan','Crisan',3265552)] )
    
    def test_setters(self): 
        self.__plane1.setAirlineCompany('BlueAir')
        self.assertEqual(self.__plane1.getAirlineCompany(), 'BlueAir')

        self.__plane1.setNumberSeats(155)
        self.assertEqual(self.__plane1.getNumberSeats(), 155)
        
        self.__plane1.setDestination('London')
        self.assertEqual(self.__plane1.getDestination(), 'London')
        
        list1=[Passenger('Marius','Faur',225296)]
        self.__plane1.setListPassengers(list1)
        self.assertEqual(self.__plane1.getListPassengers(), [Passenger('Marius','Faur',225296)])
        
        self.__plane1.setName('N-776')
        self.assertEqual(self.__plane1.getName(), 'N-776')
        
    def test_raises_number_of_seats(self):
        self.assertRaises(ValueError, lambda: self.__plane1.setNumberSeats('-99.5'))
        self.assertRaises(ValueError, lambda: self.__plane1.setNumberSeats('asa'))