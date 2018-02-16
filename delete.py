#importing libraries
import urllib
from bs4 import BeautifulSoup
#taking inputs
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
position = input('Enter the position: ')
count = input('Enter the count: ')

#repeating the count

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
print(soup.prettify)
    #url=html
"""
    if i < count :
        print('Retrieving...', url)
    else :
        print ('Retrieving...', url)
        break
    # collecting all anchor tags
    tags = soup('a')

    #finding the tag position
    tag_position = 0
    for tag in tags :
        tag_position += 1
        if tag_position == int(position) :
            url = tag.get('href')
            if i == int(count) - 1 :
                #printing the output
                print (tag.contents[0])
                break
"""
