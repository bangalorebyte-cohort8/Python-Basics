"""
Challenge #1

Using the file "words.txt" in this repo, write a function that reads the words
in words.txt and stores them as keys in a dictionary. It doesn’t matter what the
values are. Use the 'in' operator to find if a word is in the dictionary.
"""

def searchword(w) :
    #print(w)

    #opening a file
    fhandle=open('words.txt')

    #initializing the dictionary
    dictionary={}

    #storing all the words in a dictionary
    for word in fhandle :
        dictionary[word]=dictionary.get(word,0)+1
    #return dictionary

    #printing all the words stored as keys in the dictionary.
    for key in dictionary.keys():
        if w==key.rstrip() : return True
    return False

#printing return value and calling the function. 
print(searchword(input( " Enter the word to search for " )))
