"""
Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Hint: Use a tuple

"""


from operator import itemgetter

def freq_counter(line) :

    dictionary={}
    list_a=[]

    for char in line :
        dictionary[char]=dictionary.get(char,0)+1

    for key,value in dictionary.items() :

        list_a.append([key,value])
        list_a.sort(key=itemgetter(1),reverse=True)

    return list_a




line = input( "Enter the string").strip()
list_b=freq_counter(line)

for i in list_b :
    print(str(i).strip('[]'))
