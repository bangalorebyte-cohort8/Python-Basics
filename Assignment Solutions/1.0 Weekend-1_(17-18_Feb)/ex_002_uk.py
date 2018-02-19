"""
Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are square of keys.
"""

"""
Remark from Udit :  the Question doesnot explictly specify the input criteria : therefore an asumption
has been made that the programmer inputs the dictioneuy values
"""


import random

#Defining the function to print out the key and values which satisfy the mentioned criteria
def selection (dictionary) :
    for key,value in dictionary.items() :
        if key >=1 and key<=3 :
            if value==key**2 :
                print(key,value)


#Taking User Inputs

n= int(input ( " Enter the dictionary Size "))
dictionary={}

for i in range(n) :
    x =int(input ( " Enter the key number " ))
    y =int(input ( " Enter the Value Number "))
    dictionary[x]=dictionary.get(x,y)


#Calling the Function and printing the return Value
selection(dictionary)
