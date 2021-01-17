'''
Created on Dec 12, 2019

@author: PAnita
'''
import unittest
from Repository.RepositoryPlanes import PlaneRepository
from Domain.Passenger import Passenger
from Domain.Plane import Plane
from builtins import staticmethod

class TestPlaneRepository(unittest.TestCase):

    def setUp(self):
        passenger1=Passenger('Ana','Pop',5563525)
        passenger2=Passenger('Andreea','Mare',55695145)
        passenger3=Passenger('Andrei','Paunescu',6355985)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        passenger5=Passenger('Marius','Faur',225296)
        passenger6=Passenger('Andrei','Mare', 29965)
        
        list1=[passenger1,passenger2,passenger4]
        list2=[passenger3,passenger5,passenger4]
        list3=[passenger6]
        
        self.__repo=PlaneRepository()
        self.__repo.add_plane("Ak-44", "WizzAir", 55, "Paris", list1)
        self.__repo.add_plane("TR-322", "BlueAir", 122, "Monaco", list2)
        self.__repo.add_plane("SS-989", "BlueAir", 99, "Paris", list3)
        
        #Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers())
        #Plane("TR-322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers())
        #Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers())
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

###################################################
    @staticmethod
    def return_list1_passengers():
        passenger1=Passenger('Ana','Pop',5563525)
        passenger2=Passenger('Andreea','Mare',55695145)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        list1=[passenger1,passenger2,passenger4]
        return list1
    
    @staticmethod
    def return_list2_passengers():
        passenger3=Passenger('Andrei','Paunescu',6355985)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        passenger5=Passenger('Marius','Faur',225296)
        list2=[passenger3,passenger5,passenger4]
        return list2
    
    @staticmethod
    def return_list3_passengers():
        passenger6=Passenger('Andrei','Mare', 29965)
        list3=[passenger6]
        return list3
##################################################        
 
 
#Updates on plane#
    def test_update_name_by_plane_name(self):
        self.assertEqual((self.__repo.update_name_by_plane_name('Ak-44', 'SS-88'))[0], Plane('SS-88', "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()))
    
    def test_update_company_by_plane_name(self):
        self.assertEqual((self.__repo.update_company_by_plane_name('Ak-44', 'BlueAir'))[0], Plane("Ak-44", "BlueAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()))
    
    def test_update_noSeats_by_plane_name(self):
        self.assertEqual((self.__repo.update_noSeats_by_plane_name('Ak-44', 125))[0], Plane("Ak-44", "WizzAir", 125, "Paris", TestPlaneRepository.return_list1_passengers()))
    
    def test_update_destination_by_plane_name(self):
        self.assertEqual((self.__repo.update_destination_by_plane_name('Ak-44', 'London'))[0], Plane('Ak-44', "WizzAir", 55, "London", TestPlaneRepository.return_list1_passengers()))
    
    def test_update_list_of_passengers_by_plane_name(self):
        passenger3=Passenger('Andrei','Paunescu',6355985)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        passenger5=Passenger('Marius','Faur',225296)
        list2=[passenger3,passenger5,passenger4]
        self.assertEqual((self.__repo.update_list_of_passengers_by_plane_name('Ak-44', list2))[0], Plane('Ak-44', "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()+list2 ))
        
    
#Updates on passengers#
    def test_update_passenger_by_name(self):
        new_list_passengers=TestPlaneRepository.return_list1_passengers()[:]
        new_list_passengers[0].setFirstName('Anca')
        new_list_passengers[0].setLastName('Popa')
        new_list_passengers[0].setPassport(334556)
        self.assertEqual((self.__repo.update_passenger_by_name('Ana','Pop','Anca', 'Popa', 334556 ))[0], Plane('Ak-44', "WizzAir", 55, "Paris", new_list_passengers ))
    
        
#Delete#
    def test_delete_plane_by_name(self):
        self.assertEqual(self.__repo.delete_plane_by_name('TR-322'), [Plane('Ak-44', "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()),Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers())])
        
    def test_delete_passenger_by_name(self):
        new_list_passengers=TestPlaneRepository.return_list1_passengers()[1:]
        self.assertEqual((self.__repo.delete_passenger_by_name('Ana', 'Pop'))[0], Plane('Ak-44', "WizzAir", 55, "Paris", new_list_passengers))


#Return#
    def test_return_planes_no_passengers_lower_than_n(self):
        self.assertEqual( self.__repo.return_planes_no_passengers_lower_than_n(1) , [ ] )
        self.assertEqual( self.__repo.return_planes_no_passengers_lower_than_n(3) , [Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers())] )
        #self.assertEqual( self.__repo.return_planes_no_passengers_lower_than_n(5) , [Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()), Plane("233322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers()), Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers())] )

    def test_return_passenger_name_starting_with_string(self):
        self.assertEqual(self.__repo.return_passenger_name_starting_with_string('Ak-44','An'), [Passenger('Ana','Pop',5563525),Passenger('Andreea','Mare',55695145)])

    def test_return_planes_with_destination(self):
        self.assertEqual(self.__repo.return_planes_with_destination('Paris'), [Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()),Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers())])
        
        
#Sort and search#
    def test_sort_passengers_by_last_name(self):
        passenger1=Passenger('Ana','Pop',5563525)
        passenger2=Passenger('Andreea','Mare',55695145)
        passenger4=Passenger('Bogdan','Crisan',3265552)
        list_sorted=[passenger4,passenger2,passenger1]
        self.assertEqual((self.__repo.sort_passengers_by_last_name('Aka-44'))[0], Plane("Ak-44", "WizzAir", 55, "Paris", list_sorted) )
    
    def test_sort_planes_by_no_passengers(self):
        self.assertEqual(self.__repo.sort_planes_by_no_passengers(), [Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers()),Plane("TR-322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers()),Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers())])
        
    def test_sort_planes_by_no_passengers_first_name_substr(self):
        self.assertEqual(self.__repo.sort_planes_by_no_passengers_first_name_substr('An'), [Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()), Plane("SS-989", "BlueAir", 99, "Paris", TestPlaneRepository.return_list3_passengers()), Plane("TR-322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers())])
    
    #verifica asta dupa modificari (merge, rescrie test)
    #def test_sort_concatenation(self):
        #self.assertEqual((self.__repo.sort_concatenation())[0], Plane("TR-322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers()))
        
    def test_identify_passengers_passport(self):
        self.assertEqual(self.__repo.identify_passengers_passport(), [Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers())])
    
    def test_identify_passenger_with_given_string(self):
        self.assertEqual(self.__repo.identify_passenger_with_given_string('Ak-44', 're' ), [Passenger('Andreea','Mare',55695145)])
        self.assertEqual(self.__repo.identify_passenger_with_given_string('Ak-44', 'ke' ), [ ])
        
    def test_identify_plane_with_passenger(self):
        self.assertEqual(self.__repo.identify_plane_with_passenger('Bogdan', 'Crisan'),[Plane("Ak-44", "WizzAir", 55, "Paris", TestPlaneRepository.return_list1_passengers()), Plane("TR-322", "BlueAir", 122, "Monaco", TestPlaneRepository.return_list2_passengers())] )
    
       
#Form groups
    
    