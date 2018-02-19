"""
You are required to write a program to sort the (name, age, height) tuples by
ascending order where name is string, age and height are numbers.

The sort criteria is:

1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.

The priority is that name > age > score.

If the following tuples are given as input to the program:
Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85

1 2
5 6
9 10

Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '100', '91'),
('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Enjoy!!

"""
from operator import itemgetter
#taking the range

n=int(input( 'Enter the range '))

list_a=[]

if n==0 :
    list_a= [('Tom',19,80), ('John',20,90), ('Jony',17,93), ('Jony',17,91), ('Json',21,85)]

else :
    for i in range(n) :
        list_a.append(tuple(input( " Enter the Name Age and score :  " ).split(',')))

temp1=sorted(list_a,key=itemgetter(0,1,2))
print(temp1)

#print(sorted(list_a,key=itemgetter(0)))
#print(sorted(temp2,key=itemgetter(0,1,2)))

#print(list_a.itemgetter(0))
#print(list_a)



#list_a.sort(key=itemgetter(0))
#list_a.sort(key=itemgetter(1))
#list_a.sort(key=itemgetter(2),reverse=True)


#print(list_a)
