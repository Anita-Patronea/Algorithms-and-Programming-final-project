'''
Created on Jan 5, 2020

@author: PAnita
'''
from builtins import staticmethod
from Domain.Passenger import Passenger

class Controller():

    def __init__(self, repo):
        '''
        Constructor
        '''
        self.__repo=repo
        
    def controller_add_plane(self, nameNo, company, noSeats, destination, listPassengers):
        self.__repo.add_plane(nameNo, company, noSeats, destination, listPassengers)
        
    def controller_get_planes(self):
        return self.__repo
        
    def controller_update_name_by_plane_name(self,name,new_name):
        return self.__repo.update_name_by_plane_name(name,new_name) 
    
    def controller_update_company_by_plane_name(self,name,new_company):
        return self.__repo.update_company_by_plane_name(name,new_company)
    
    def controller_update_noSeats_by_plane_name(self,name,new_noSeats):
        return self.__repo.update_noSeats_by_plane_name(name,new_noSeats)
    
    def controller_update_destination_by_plane_name(self,name, new_destination):
        return self.__repo.update_destination_by_plane_name(name, new_destination)
    
    def controller_update_list_of_passengers_by_plane_name(self, name, new_listPassengers):
        return self.__repo.update_list_of_passengers_by_plane_name(name, new_listPassengers)
    
    def controller_update_passenger_by_name(self,first_name,last_name, new_first_name,new_last_name, new_passport):
        return self.__repo.update_passenger_by_name(first_name,last_name, new_first_name,new_last_name, new_passport)
    
    def controller_delete_plane_by_name(self,name):
        return self.__repo.delete_plane_by_name(name)
    
    def controller_delete_passenger_by_name(self,first_name, last_name):
        return self.__repo.delete_passenger_by_name(first_name, last_name)
    
    def controller_return_planes_no_passengers_lower_than_n(self,no):
        new_list=""
        for plane in self.__repo.return_planes_no_passengers_lower_than_n(no):
            s=""
            s=s+str(plane)
            new_list=new_list+s+"\n"
        return new_list
    
    def controller_return_passenger_name_starting_with_string(self,plane_name,string_given):
        new_list=""
        for person in self.__repo.return_passenger_name_starting_with_string(plane_name,string_given):
            s=""
            s=s+str(person)+"\n"
            new_list=new_list+s
        return new_list
    
    def controller_return_planes_with_destination(self,destination):
        new_list=""
        for plane in self.__repo.return_planes_with_destination(destination):
            s=""
            s=s+str(plane)
            new_list=new_list+s+"\n"
        return new_list

    def controller_sort_passengers_by_last_name(self,plane_given):
        return self.__repo.sort_passengers_by_last_name(plane_given)
    
    def controller_sort_planes_by_no_passengers(self):
        return self.__repo.sort_planes_by_no_passengers()
    
    def controller_sort_planes_by_no_passengers_first_name_substr(self,substring):
        return self.__repo.sort_planes_by_no_passengers_first_name_substr(substring)
    
    def controller_sort_concatenation(self):
        return self.__repo.sort_concatenation()
    
    def controller_identify_passengers_passport(self):
        new_list=""
        for plane in self.__repo.identify_passengers_passport():
            s=""
            s=s+str(plane)
            new_list=new_list+s+"\n"
        return new_list       
    
    def controller_identify_passenger_with_given_string(self, plane_given, substring):
        new_list=""
        for person in self.__repo.identify_passenger_with_given_string(plane_given, substring):
            s=""
            s=s+str(person)+"\n"
            new_list=new_list+s
        return new_list

    def controller_identify_plane_with_passenger(self, first_name_given, last_name_given):
        new_list=""
        for plane in self.__repo.identify_plane_with_passenger(first_name_given, last_name_given):
            s=""
            s=s+str(plane)
            new_list=new_list+s+"\n"
        return new_list 
    
    def controller_form_groups_of_passengers(self,plane_given, k):
        new_list=""
        for person in self.__repo.form_groups_of_passengers(plane_given, k):
            s=""
            s=s+str(person)+"\n"
            new_list=new_list+s
        return new_list
    
    def controller_form_groups_of_planes(self, k):
        new_list=""
        for plane in self.__repo.form_groups_of_planes(k):
            s=""
            s=s+str(plane)
            new_list=new_list+s+"\n"
        return new_list         
    
    @staticmethod
    def controller_create_object_PASSENGER(first_name, last_name, passport_number):
        return Passenger(first_name, last_name, passport_number)
        
    
    
    
    
    