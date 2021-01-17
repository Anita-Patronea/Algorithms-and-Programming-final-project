'''
Created on Dec 12, 2019

@author: PAnita
'''


class Passenger():
    '''
    This class creates objects of type passenger (identified by first name-str, last name-str and passport number-int)
    '''
    
    def __init__(self, firstN, lastN, passportNo):
        '''
        Constructor
        '''
        self.__first_name=firstN
        self.__last_name=lastN
    
        try: 
            passportNo_converted=int(passportNo)
            if passportNo_converted>0:
                self.__passport_number=passportNo_converted
            else:
                raise ValueError("Invalid passport number! Please insert a positive integer.")
        except:
            raise TypeError("Invalid passport number! Please insert an integer.")
    
    
    def __str__(self):
        s="   "
        s=s+str(self.__first_name)+" "+str(self.__last_name)+"     ID: "+str(self.__passport_number)
        return s
    
    
    def __eq__(self,other):
        if self.__first_name==other.__first_name and self.__last_name==other.__last_name and self.__passport_number==other.__passport_number:
            return True
        else:
            return False
    
    
    def getFirstName(self):
        return  self.__first_name
    
    def getLastName(self):    
        return self.__last_name
    
    def getPassport(self):
        return self.__passport_number
    
    
    def setFirstName(self,firstN):
        self.__first_name=firstN
        
    def setLastName(self,lastN):
        self.__last_name=lastN
        
    def setPassport(self,passportNo):
        try: 
            passportNo_converted=int(passportNo)
            if (passportNo_converted>0):
                self.__passport_number=passportNo_converted
            else:
                raise TypeError
        except:
            raise TypeError("Invalid passport number! Please give a positive integer.")