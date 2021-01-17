'''
Created on Jan 9, 2020

@author: PAnita
'''
def my_search(my_list, my_condition):
    for i in range (0, len(my_list)):
        if my_condition(my_list[i]):
            return my_list[i]
                
def test_my_search():
    assert(my_search([22,6,9], lambda x: x==6) == 6)
    assert(my_search([22,6,9], lambda x: x==10) == None)
    
test_my_search()  
  
    

    