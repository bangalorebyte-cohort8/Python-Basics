"""
Two words are “rotate pairs” if you can rotate one of them and get the other
(see above problem) Write a program that reads a wordlist and finds all the
rotate pairs. Hint: Use a dictionary


Remarks by Udit :

Concept : if the difference in the ord values of each characted of 2 words is same
then those words are rotated pairs

"""

def check (word1,word2) :
    list_a=[]

    for i in range(len(word1)):
        temp=ord(word1[i])-ord(word2[i])
        list_a.append(temp)

    if max(list_a)!=min(list_a):
        return False
    else : return True



def count__rotate_pairs (abc):

    for word in abc :

        temp=word
        abc.remove(word)

        for re in abc :

            if len(temp)== len(re):

                if check (temp,re)==True:
                    print(temp,re)


#taking user inputs and calling the function.

abc=input( " Enter the list of words separated by comma  :  ").split(',')
count__rotate_pairs(abc)






"""
Implementation  :

abc = 294
bcd = 297

Error in logic:

aaa
abc


rotated by 1 : difference between 2 words is 3 : len of abc =3 -> diff should be
divisible by len

concept explanation :

x+y+z = t
(x+r) + (y+r)+ (z+r) = l
(x+y+z) + (3*r)= l
t + 3r = l
3r = l-t

r= (l-t) / 3 —> should be divisible by 3 ! in this case
—> diff of sum of 2 words should be divisible by  number of characters in each word.



lenght of 2 words should be equal :

above Concept
"""
