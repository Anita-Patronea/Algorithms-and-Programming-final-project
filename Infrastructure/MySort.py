'''
Created on Jan 4, 2020

@author: PAnita
'''
def my_sort(myList, myCondition):
    for i in range (0,len(myList)-1):
        for j in range (i+1, len(myList)):
            if not myCondition(myList[i],myList[j]):
                myList[i],myList[j]=myList[j],myList[i]
    return myList

def test_my_sort():
    assert(my_sort([2,4,1,-3], lambda x,y: x<y) == [-3,1,2,4])
    assert(my_sort([1,2,4], lambda x,y: x<y) == [1,2,4])
    assert(my_sort([2,0,9,-5,6,8,7], lambda x,y: x<y)==[-5,0,2,6,7,8,9])
 
test_my_sort()