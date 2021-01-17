'''
Created on Dec 12, 2019

@author: PAnita
'''
    
class Plane():
    '''
    This class creates objects of type plane ( (identified by name/number-str, airline company-str, number of seats-positive integer, destination-str, list of passengers)
    
    '''
    
    def __init__(self, nameNo, company, noSeats, destination, listPassengers=[]):
        '''
        Constructor
        '''
        self.__name=nameNo
        
        self.__airline_company=company
        
        try:
            noSeats_converted=int(noSeats)
            if noSeats_converted>0:
                self.__number_seats=noSeats_converted
            else:
                raise ValueError("Invalid number of seats! Please give a positive integer.")
        except:
            raise TypeError("Invalid number of seats! Please give a positive integer not a string.")
        
        self.__destination=destination
        
        self.__list_passengers=listPassengers
            
    
    def __str__(self):
        s=""
        s=s+"Company name: "+str(self.__airline_company)+"\n"
        s=s+"Plane name/number: "+str(self.__name)+"\n"
        s=s+"Destination: "+str(self.__destination)+"\n"
        s=s+"Number of seats: "+str(self.__number_seats)+"\n"
        s=s+"Passengers: "+"\n"
        for pers in self.__list_passengers:
            s=s+str(pers)+"\n"
        return s
    
    
    def __eq__(self,other):
        ok1=0
        if self.__airline_company==other.__airline_company and self.__destination==other.__destination and self.__name==other.__name and self.__number_seats==other.__number_seats:
            ok1=1
            
        len_list_passengers_self=len(self.__list_passengers)
        len_list_passengers_other=len(other.__list_passengers)
        
        ok2=1
        if(len_list_passengers_other==len_list_passengers_self):
            for elem in self.__list_passengers:
                if not (elem in other.__list_passengers):
                    ok2=0
        else:
            ok2=0
        
        if(ok1==1 and ok2==1):
            return True
        else:
            return False
                    
                
               
    def getName(self):
        return self.__name
    
    def getAirlineCompany(self):
        return self.__airline_company
    
    def getNumberSeats(self):
        return self.__number_seats
    
    def getDestination(self):
        return self.__destination
    
    def getListPassengers(self):
        return self.__list_passengers
    
    def getNumberOfPassengers(self):
        return len(self.__list_passengers)
    
    
    
    def setName(self,nameNo):
        self.__name=nameNo
        
    def setAirlineCompany(self,company):
        self.__airline_company=company
        
    def setNumberSeats(self,noSeats):
        try:
            noSeats_converted=int(noSeats)
            if noSeats_converted>0:
                self.__number_seats=noSeats_converted
            else:
                raise ValueError
        except:
            raise ValueError("Invalid number of seats! Please give a positive integer.")
    
    def setDestination(self,destination):
        self.__destination=destination
        
    def setListPassengers(self,listPassengers):
        self.__list_passengers=listPassengers
        
        
 
        