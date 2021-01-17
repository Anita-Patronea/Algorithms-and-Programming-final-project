'''
Created on Jan 8, 2020

@author: PAnita
'''
from builtins import staticmethod
from Application.Controller import Controller


class UI():
    '''
    Menu for plane repository
    '''


    def __init__(self, service):
        '''
        Constructor
        '''
        self.__service=service
        
###################################################################    
    @staticmethod
    def print_welcome():
        print("Hello there!")
        
    @staticmethod
    def print_menu():
        print("This program manages several planes and allows operations such as: ")
        print("1. Add a new plane to the repository")
        print("2. Get all the planes")
        print("3. Update a plane")
        print("4. Update a passenger")
        print("5. Delete a plane by giving its name")
        print("6. Delete a passenger by giving his name")
        print("7. Return planes with the number of passengers lower than a given number")
        print("8. Return passengers from a given plane that have the first name starting with a given string")
        print("9. Return planes with a given destination")
        print("10. Sort the passengers in a plane by their last name")
        print("11. Sort planes according to the number of passengers")
        print("12. Sort planes according to the number of passengers with the first name starting with a given substring")
        print("13. Sort planes according to the string obtained by the concatenation of the number of passengers in the plane and the destination")
        print("14. Identify planes that have passengers with passport numbers starting with the same 3 letters")
        print("15. Identify passengers from a given plane for which the first name or last name contain a string given as parameter")
        print("16. Identify plane/planes where there is a passenger with given name")
        print("17. Form groups of k passengers from the same plane but with different last names (k is a value given by the user)")
        print("18. Form groups of k planes with the same destination but belonging to different airline companies (k is a value given by the user)")
        print("0. Exit")
        print("\n")
        
    @staticmethod
    def print_sub_menu_for_plane_updates():
        print("1. Update the name of a plane")
        print("2. Update the airline company name of a plane")
        print("3. Update the number of seats of a plane ")
        print("4. Update the destination of a plane")
        print("5. Update the list of passengers of a plane ")

     
####################################################################################      
    @staticmethod
    def user__option():
        try:
            user_option=int(input("Please give an option: "))
            return user_option
        except TypeError:
            print("Please give a valid option!")
            UI.user__option()
            
    #############
    @staticmethod
    def read_plane_name():
        name=input("Give the name of the plane: ")
        return name
    
    @staticmethod
    def read_plane_airline_company():
        company=input("Give the company name of the plane: ")
        return company
    
    @staticmethod
    def read_plane_number_of_seats():
        number=int(input("Give the number of seats of the plane: "))
        return number
    
    @staticmethod
    def read_plane_destination():
        destination=input("Give the destination of the plane: ")
        return destination
    
    @staticmethod
    def read_plane_list_of_passengers():
        number_of_passengers=int(input("Give the number of passengers you want to add: "))
        passenger_list=[]
        
        while number_of_passengers>0:
            f=UI.read_passenger_first_name()
            l=UI.read_passenger_last_name()
            p=UI.read_passenger_passport_number()
            new_passenger=Controller.controller_create_object_PASSENGER(f, l, p)
            passenger_list.append(new_passenger)
            number_of_passengers=number_of_passengers-1
            
        return passenger_list
        
    @staticmethod
    def read_passenger_first_name():
        first_name=input("Give the first name of the passenger: ")
        return first_name
    
    @staticmethod
    def read_passenger_last_name():
        last_name=input("Give the last name of the passenger: ")
        return last_name   
     
    @staticmethod
    def read_passenger_passport_number():
        passport=input("Give the passport number of the passenger: ")
        return passport
        
    
###################################################################################
    def main_menu(self):
        UI.print_welcome()
        print("\n")
        while (True):
            try:
                UI.print_menu()
                option=UI.user__option()
                
                if(option==0):
                    print("Bye! Bye!")
                    return
                
                elif(option==1):
                    name = UI.read_plane_name()
                    company = UI.read_plane_airline_company()
                    no_seats = UI.read_plane_number_of_seats()
                    destination = UI.read_plane_destination()
                    list_passengers = UI.read_plane_list_of_passengers()
                    self.__service.controller_add_plane(name,company,no_seats,destination,list_passengers)
                    
                elif(option==2):
                    print(self.__service.controller_get_planes())
                    
                elif(option==3):
                                try:
                                    UI.print_sub_menu_for_plane_updates()
                                    option=UI.user__option()
                                    
                                    if(option==1):
                                        name=UI.read_plane_name()
                                        print("NEW DATA: ")
                                        new_name=UI.read_plane_name()
                                        self.__service.controller_update_name_by_plane_name(name, new_name)
                                        
                                    elif(option==2):
                                        name=UI.read_plane_name()
                                        print("NEW DATA: ")
                                        new_company=UI.read_plane_airline_company()
                                        self.__service.controller_update_company_by_plane_name(name,new_company)
                                        
                                    elif(option==3):
                                        name=UI.read_plane_name()
                                        print("NEW DATA: ")
                                        new_no_seats=UI.read_plane_number_of_seats()
                                        self.__service.controller_update_noSeats_by_plane_name(name,new_no_seats)
                                        
                                    elif(option==4):
                                        name=UI.read_plane_name()
                                        print("NEW DATA: ")
                                        new_destination=UI.read_plane_destination()
                                        self.__service.controller_update_destination_by_plane_name(name,new_destination)
                                        
                                    elif(option==5):
                                        name=UI.read_plane_name()
                                        print("NEW DATA: ")
                                        new_list=UI.read_plane_list_of_passengers()
                                        self.__service.controller_update_list_of_passengers_by_plane_name(name, new_list)
                                    
                                    else:
                                        print("Please give a valid option! ")
                                    print("\n")
                                
                                except ValueError as e:
                                    print("Something went wrong!")
                                    print(e)
                                    
                                except TypeError as e:
                                    print("Something went wrong!")
                                    print(e)
                        
                elif(option==4):
                    first_name = UI.read_passenger_first_name()
                    last_name = UI.read_passenger_last_name()
                    print("NEW DATA: ")
                    new_first_name = UI.read_passenger_first_name()
                    new_last_name = UI.read_passenger_last_name()
                    new_passport = UI.read_passenger_passport_number()
                    self.__service.controller_update_passenger_by_name(first_name, last_name, new_first_name, new_last_name, new_passport)
                    
                elif(option==5):
                    name=UI.read_plane_name()
                    self.__service.controller_delete_plane_by_name(name)
    
                elif(option==6):
                    first_name = UI.read_passenger_first_name()
                    last_name = UI.read_passenger_last_name()
                    self.__service.controller_delete_passenger_by_name(first_name, last_name)
                    
                elif(option==7):
                    number_passengers = int(input("Give the limit number of passengers: "))
                    print(self.__service.controller_return_planes_no_passengers_lower_than_n(number_passengers))
                    
                elif(option==8):
                    name = UI.read_plane_name()
                    read_string=input("Give the string: ")
                    print(self.__service.controller_return_passenger_name_starting_with_string(name, read_string))
                    
                elif(option==9):
                    destination = UI.read_plane_destination()
                    print(self.__service.controller_return_planes_with_destination(destination))
                    
                elif(option==10):
                    name = UI.read_plane_name()
                    self.__service.controller_sort_passengers_by_last_name(name)
                    
                elif(option==11):
                    self.__service.controller_sort_planes_by_no_passengers()
                    
                elif(option==12):
                    read_string=input("Give the string: ")
                    self.__service.controller_sort_planes_by_no_passengers_first_name_substr(read_string)
                    
                elif(option==13):
                    self.__service.controller_sort_concatenation()
                    
                elif(option==14):
                    print(self.__service.controller_identify_passengers_passport())
                    
                elif(option==15):
                    name = UI.read_plane_name()
                    read_string=input("Give the string: ")
                    print(self.__service.controller_identify_passenger_with_given_string(name, read_string))
                    
                elif(option==16):
                    first_name=UI.read_passenger_first_name()
                    last_name=UI.read_passenger_last_name()
                    print(self.__service.controller_identify_plane_with_passenger(first_name, last_name))
                elif(option==17):
                    name = UI.read_plane_name()
                    k=int(input("Please give the length, k (natural number): "))
                    print(self.__service.controller_form_groups_of_passengers(name, k))
                elif(option==18): 
                    k=int(input("Please give the length, k (natural number): "))
                    print(self.__service.controller_form_groups_of_planes(k))
                    
                else:
                    print("Please give a valid option! ")
                print("\n")
            
            except ValueError as e:
                print("Something went wrong!")
                print(e)
                print("\n")
                
            except TypeError as e:
                print("Something went wrong!")
                print(e)
                print("\n")
                
    


    
    
    
    
    
    
        
        
        