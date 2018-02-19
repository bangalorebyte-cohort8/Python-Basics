"""
Challenge #1

Using the file "words.txt" in this repo, write a function that reads the words
in words.txt and stores them as keys in a dictionary. It doesn’t matter what the
values are. Use the 'in' operator to find if a word is in the dictionary.

"""



fhandle=open('words.txt')

dictionary={}

for line in fhandle :
    for word in line :
        dictionary[word]=dictionary.get(word,0)+1
print(dictionary)
