"""
infinite monkey theorem -
methinks it is like a weasel
"""

import random

"""

shak=list('abc')
#shak=shak.replace(' ','')
#print(shak)

#initiliazing the lists to store the new generated list and the turn at which it matches
monkey=[]
jackpot=[]

#function to generate random characters - lower case alphabets


print(randrange('a','z',3))

#print(guess())

#initializing the count to keep track if number of iterations.
count=0


#for loop to iterate over each alphabet and comapare with random generator for a match.

for i in shak :
    x=guess()
    print(x)
    print(i)


    if i==' ' :
        monkey.append(i)
    while i!= x:
        #print(i)
        count+=1
        print(count)
        if count%1000==0 :
            print(" At 1000 th Iteration following string has been matched. ")
            print(str(monkey))

    if i==x:
        monkey.append(i)
        jackpot.append(count)
        print(monkey)
        count=0


    if count==1000 :
        print(" At 1000 th Iteration following string has been matched. ")
        print(str(monkey))

print(monkey)
print(jackpot)
"""




















def play(n) :
    temp=''
    for i in range(n) :
        temp+=chr(random.randrange(97,123,1))
        #temp+=chr(x)
    return temp



def machine(jackpot) :
    count=0
    temp=''
    while jackpot!=temp :
        temp=play(len(jackpot))
        count+=1
        sucess= (1/count)*100
        print(count)
    print(temp)
    print( " Number Of Iterations " , count)
    return sucess


jackpot=input( " Enter the string you want to input " )

print ("Sucess percentage = " , machine(jackpot) )

"""
part-2 keep the characters which are a match and only find the others - also account for the spaces"""
#print((play(4)))
