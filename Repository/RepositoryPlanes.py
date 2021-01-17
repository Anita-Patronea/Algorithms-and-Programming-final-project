'''
Created on Dec 12, 2019

@author: PAnita
'''
from Domain.Plane import Plane
from itertools import combinations
from Infrastructure import MySort



class PlaneRepository():
    def __init__(self):
        '''
        Constructor
        '''
        self.__repo=[]    
        
        
    def add_plane(self, nameNo, company, noSeats, destination, listPassengers=[]):
        self.__repo.append(Plane(nameNo,company,noSeats,destination,listPassengers))
        
        
    def __str__(self):
        s=""
        s=s+"The planes of the airport are : "+"\n"+"\n"
        for plane in self.__repo:
            s=s+str(plane)+"\n"+"\n"
        return s
    
    
    def __eq__(self,other):
        len_repo_self=len(self.__repo)
        len_repo_other=len(other.__repo)
        
        ok=1
        if(len_repo_other==len_repo_self):
            for elem in self.__repo:
                if not (elem in other.__repo):
                    ok=0
        else:
            ok=0
        
        if  ok==1:
            return True
        else:
            return False
        
        
        
        
    '''CRUD'''   
    
    ###Updates on PLANE###
    #Update the name of a plane 
    def update_name_by_plane_name(self,name,new_name):
        for plane in self.__repo:
            if plane.getName()==name:
                plane.setName(new_name)
        return self.__repo
    #Update the company name of a plane 
    def update_company_by_plane_name(self,name,new_company):
        for plane in self.__repo:
            if plane.getName()==name:
                plane.setAirlineCompany(new_company)
        return self.__repo
    
    #Update the number of seats of a plane 
    def update_noSeats_by_plane_name(self,name,new_noSeats):
        for plane in self.__repo:
            if plane.getName()==name:
                plane.setNumberSeats(new_noSeats)
        return self.__repo
    
    #Update the destination of a plane
    def update_destination_by_plane_name(self,name, new_destination):
        for plane in self.__repo:
            if plane.getName()==name:
                plane.setDestination(new_destination)
        return self.__repo
     
    #Update the list of passengers of a plane            
    def update_list_of_passengers_by_plane_name(self, name, new_listPassengers):
        updated_list=[]
        for plane in self.__repo:
            if plane.getName()==name:
                updated_list=plane.getListPassengers()[:]
                for passenger in new_listPassengers:
                    updated_list.append(passenger)
                plane.setListPassengers(updated_list)
        return self.__repo
    
    
    ###Updates on PASSENGER###
    #Update a passenger
    def update_passenger_by_name(self,first_name,last_name, new_first_name,new_last_name, new_passport):
        for plane in self.__repo:
            for passenger in plane.getListPassengers():
                if passenger.getFirstName()==first_name and passenger.getLastName()==last_name:
                    passenger.setFirstName(new_first_name)
                    passenger.setLastName(new_last_name)
                    passenger.setPassport(new_passport)
        return self.__repo
    
    
    ###Delete a PLANE###
    def delete_plane_by_name(self,name):
        for plane in self.__repo:
            if plane.getName()==name:
                self.__repo.remove(plane)
        return self.__repo
        
        
    ###Delete a PASSENGER###
    def delete_passenger_by_name(self,first_name, last_name):
        for plane in self.__repo:
            for passenger in plane.getListPassengers():
                if passenger.getFirstName()==first_name and passenger.getLastName()==last_name:
                    plane.getListPassengers().remove(passenger)
        return self.__repo
    
    
    ###Return planes with the number of passengers lower than a given number###
    def return_planes_no_passengers_lower_than_n(self,no):
        new_repo=[]
        for plane in self.__repo:
            if plane.getNumberOfPassengers()<no:
                new_repo.append(plane)
        return new_repo
    
    
    ###Return passengers from a given plane that have the first name starting with a given string###
    def return_passenger_name_starting_with_string(self,plane_name,string_given):
        new_list_passengers=[]
        for plane in self.__repo:
            if plane.getName()==plane_name:
                for passenger in plane.getListPassengers():
                    result=passenger.getFirstName().startswith(string_given)
                    if result==True:
                        new_list_passengers.append(passenger)
        return new_list_passengers
    
    
    ###Return planes with a given destination###
    def return_planes_with_destination(self,destination):
        new_repo=[]
        for plane in self.__repo:
            if plane.getDestination()==destination:
                new_repo.append(plane)
        return new_repo
      
    
    
    '''Sort and search'''
    ###Sort the passengers in a plane by last name##
    def sort_passengers_by_last_name(self,plane_given):
        for plane in self.__repo:
            if plane.getName()==plane_given:
                #Sorted with my sorting algorithm
                MySort.my_sort(plane.getListPassengers(), lambda x,y: x.getLastName()<y.getLastName())
                #plane.getListPassengers().sort(key=lambda Passenger: Passenger.getLastName())
        return self.__repo
    
    ###Sort planes according to the number of passengers
    def sort_planes_by_no_passengers(self):
        #Sorted with my sorting algorithm
        MySort.my_sort(self.__repo, lambda x,y: x.getNumberOfPassengers()<y.getNumberOfPassengers())
        #self.__repo.sort(key=lambda Plane: Plane.getNumberOfPassengers())
        return self.__repo                   
    
    ###Sort planes according to the number of passengers with the first name starting with a given substring###
    def sort_planes_by_no_passengers_first_name_substr(self,substring):
        list_d=[]
        for plane in self.__repo:
            no=0
            for passenger in plane.getListPassengers():
                if passenger.getFirstName().startswith(substring)==True:
                    no=no+1
            new_elem=dict(Plane=plane, No_pass_acc_cond=no)
            list_d.append(new_elem)
        #Sorted with my sorting algorithm
        MySort.my_sort(list_d, lambda x,y: x.get("No_pass_acc_cond")>y.get("No_pass_acc_cond"))
        #list_d.sort(key=lambda x: x.get("No_pass_acc_cond"))
        sorted_list=[]
        for elem in list_d:
            plane=elem.get("Plane")
            sorted_list.append(plane)
        self.__repo=sorted_list[:]
        return self.__repo
        
    ###Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination###
    def sort_concatenation(self):
        #Sorted with my sorting algorithm
        MySort.my_sort(self.__repo, lambda x,y: (str(x.getNumberOfPassengers())+x.getDestination())<(str(y.getNumberOfPassengers())+y.getDestination()))
        return self.__repo
    
    
    ###Identify planes that have passengers with passport numbers starting with the same 3 letters###
    def identify_passengers_passport(self):
        new_repo=[]
        ok=0
        for plane in self.__repo:
            for i in range (0, plane.getNumberOfPassengers()-1):
                for j in range (i+1, plane.getNumberOfPassengers()):
                    if str(plane.getListPassengers()[i].getPassport())[0:3]==str(plane.getListPassengers()[j].getPassport())[0:3]:
                        ok=1
            if ok==1:
                new_repo.append(plane)
            ok=0
        return new_repo
            
    ###Identify passengers from a given plane for which the first name or last name contain a string given as parameter###
    def identify_passenger_with_given_string(self, plane_given, substring):
        list_passengers=[]
        for plane in self.__repo:
            if plane.getName()==plane_given:
                for passenger in plane.getListPassengers():
                    if substring in passenger.getLastName() or substring in passenger.getFirstName():
                        list_passengers.append(passenger)
                #if (MySearch.my_search(plane.getListPassengers(), (lambda x, y: x.getLastName().find(substring)!=-1 or y.getFirstName().find(substring)!=-1))):
                #list_passengers.append(MySearch.my_search(plane.getListPassengers(),(lambda x, y: x.getLastName().find(substring)!=-1 or y.getFirstName().find(substring)!=-1)))
        return list_passengers
    
    ###Identify plane/planes where there is a passenger with given name###
    def identify_plane_with_passenger(self, first_name_given, last_name_given):
        list_planes=[]
        for plane in self.__repo:
            for passenger in plane.getListPassengers():
                if passenger.getFirstName()== first_name_given and passenger.getLastName()==last_name_given:
                    list_planes.append(plane)
        return list_planes
    
    '''Form groups'''

    ###Form groups of k passengers from the same plane but with different last names (k is a value given by the user)###
    def form_groups_of_passengers(self,plane_given, k):
        for plane in self.__repo:
            if plane.getName()==plane_given:
                return  list(combinations(plane.getListPassengers(),k, lambda x,y: x.getLastName()!=y.getLastName()))
    
    ###Form groups of k planes with the same destination but belonging to different airline companies (k is a value given by the user)###
    #def form_groups_of_planes(self,k):
    def form_groups_of_planes(self, k):
        #list(combinations(self.__repo, k))
        return list(list(combinations(self.__repo, k)))



