"""
ceaser cypher assignment

"""

def cypher (abc,n):

    rotate=n%26
    new_abc=''
    char=''

#iterating over each character in the string
    for letter in abc :


# small case
        if ord(letter) >=97 and ord(letter) <=122 :

            char=chr(ord(letter)+rotate)

            if ord(letter)+rotate >122 :
                char=chr(97+rotate)

            elif ord(letter)+rotate <97 :
                char=chr(122-rotate)

            new_abc+=char

    # capital case
        elif ord(letter) >=65 and ord (letter) <=90 :

            char=chr(ord(letter)+rotate)

            if ord(letter)+rotate >90 :
                char=chr(65+rotate)

            elif ord(letter)+rotate<65 :
                char=chr(90-rotate)

            new_abc+=char

    # non alphabet
        else :
            new_abc+=letter

    return new_abc

#taking user inputs and calling the function. 
abc=input( " Enter the String to be converted :  ")
n=int(input( " Enter the Number of Rotations : "))
print(cypher(abc,n))
